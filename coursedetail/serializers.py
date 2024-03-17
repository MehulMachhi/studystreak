import logging

from rest_framework import generics, serializers

from coursedetail.models import Quiz_Question, QuizOption
from master.models import (AdditionalResource, CourseMaterial,
                           LessonAssignment, LessonAttachment, batch)
from master.serializers import (AdditionalResourceListSerializers,
                                CourseMaterialListSerializers,
                                LessonAssignmentSerializer,
                                LessonAttachmentSerializer)

from .models import Lesson

logger = logging.getLogger(__name__)
# from coursedetail.serializers import QuizOptionListSerializers, Quiz_QuestionListSerializers

class Quiz_QuestionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz_Question
        fields = '__all__'

class QuizOptionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizOption
        fields = '__all__'


class LessonListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
class LessonCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        depth=3

class LessonDetailSerializer(serializers.ModelSerializer):
    attachment_lession_count = serializers.SerializerMethodField()
    attachment_lession = LessonAttachmentSerializer(many=True, read_only=True)
    quiz_question_options = serializers.SerializerMethodField()
    timestamp = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Lesson
        fields = '__all__'
        depth = 4   
    
    def get_timestamp(self, obj):
        user = self.context.get('user',None)
        if user:
            data = obj.youtube_data.filter(student=user)
            if (data.exists()):
                return data[0].timestamp
        return ""

    
    def get_attachment_lession(self, lesson):
        return LessonAttachment.objects.filter(lesson=lesson)

    def get_attachment_lession_count(self, lesson):
        attachments = LessonAttachment.objects.filter(lesson=lesson)
        serialized_attachments = LessonAttachmentSerializer(attachments, many=True).data
        return {
            'count': len(serialized_attachments),
            'attachments': serialized_attachments
        }

    def get_quiz_question_options(self, lesson):
        quiz_questions = lesson.quiz_question_set.all()
        serialized_quiz_questions = []
        for question in quiz_questions:
            quiz_options = question.quizoption_set.all()
            serialized_options = QuizOptionListSerializers(quiz_options, many=True).data
            serialized_quiz_questions.append({
                'id': question.id,
                'Question': question.Question,
                'lesson': question.lesson.id,
                'quiz_options': serialized_options
            })
        return serialized_quiz_questions
##################################################################################

        # return Quiz_QuestionListSerializers(quiz_questions, many=True).data
    
    # def get_quiz_options(self, lesson):
    #     quiz_options = QuizOption.objects.filter(name__lesson=lesson)
    #     return QuizOptionListSerializers(quiz_options, many=True).data

###############################################################################
        
######################### New code ############################################
        
# class LessonDetailSerializer(serializers.ModelSerializer):
#     attachment_lesson_count = serializers.SerializerMethodField()
#     attachment_lesson = LessonAttachmentSerializer(many=True, read_only=True)
#     quiz_data = serializers.SerializerMethodField()
#     quiz_questions = Quiz_QuestionListSerializers(many=True, read_only=True)

#     class Meta:
#         model = Lesson
#         fields = '__all__'
#         depth = 4

#     def get_attachment_lesson(self, lesson):
#         return LessonAttachment.objects.filter(lesson=lesson)

#     def get_attachment_lesson_count(self, lesson):
#         attachments = LessonAttachment.objects.filter(lesson=lesson)
#         serialized_attachments = LessonAttachmentSerializer(attachments, many=True).data
#         return {
#             'count': len(serialized_attachments),
#             'attachments': serialized_attachments
#         }

#     def get_quiz_data(self, lesson):
#         quiz_questions = Quiz_Question.objects.filter(lesson=lesson)
#         serialized_quiz_questions = Quiz_QuestionListSerializers(quiz_questions, many=True).data

#         quiz_options = QuizOption.objects.filter(name__lesson=lesson)
#         serialized_quiz_options = QuizOptionListSerializers(quiz_options, many=True).data

#         return {
#             'quiz_questions': serialized_quiz_questions,
#             'quiz_options': serialized_quiz_options
#         }


    
#############################################################################
    
class LessionRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    
    class Meta:
        model = Lesson
        fields = '__all__'
        depth = 2

class LessonCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        depth=2

class LessonCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        depth=2




from .models import Note


class NoteListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'