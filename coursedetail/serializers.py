from rest_framework import serializers
from .models import  Lesson
from rest_framework import generics
from master.serializers import (AdditionalResourceListSerializers, CourseMaterialListSerializers,
LessonAttachmentSerializer,LessonAssignmentSerializer,)
from coursedetail.models import Quiz_Question, QuizOption
from master.models import batch, CourseMaterial, AdditionalResource,LessonAttachment, LessonAssignment 
# from coursedetail.serializers import QuizOptionListSerializers, Quiz_QuestionListSerializers

class QuizOptionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizOption
        fields = '__all__'

class Quiz_QuestionListSerializers(serializers.ModelSerializer):
    quiz_options = QuizOptionListSerializers(many=True, read_only=True)
    class Meta:
        model = Quiz_Question
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
    # assignment_lession_count = serializers.SerializerMethodField()
    attachment_lession = serializers.SerializerMethodField()
    # assignment_lession = serializers.SerializerMethodField()
    quiz_questions = serializers.SerializerMethodField()
    quiz_options = serializers.SerializerMethodField()
    attachment_lession = LessonAttachmentSerializer(many=True, read_only=True)
    # assignment_lession = LessonAssignmentSerializer(many=True, read_only=True)
    quiz_questions_detail = Quiz_QuestionListSerializers(many=True, read_only=True)
    quiz_options_detail = QuizOptionListSerializers(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'
        depth = 4

    def get_attachment_lession(self, lesson):
        return LessonAttachment.objects.filter(lesson=lesson)

    # def get_assignment_lession(self, lesson):
    #     return LessonAssignment.objects.filter(lesson=lesson)

    def get_quiz_options(self, lesson):
        quiz_questions = Quiz_Question.objects.filter(lesson=lesson)
        quiz_options = QuizOption.objects.filter(name__lesson=lesson)
        serialized_quiz_question = Quiz_QuestionListSerializers(quiz_questions, many=True).data
        serialized_quiz_options = QuizOptionListSerializers(quiz_options, many=True).data
        return {
            'quiz_question': serialized_quiz_question,
            'quiz_options': serialized_quiz_options
        }

    def get_attachment_lession_count(self, lesson):
        attachments = LessonAttachment.objects.filter(lesson=lesson)
        serialized_attachments = LessonAttachmentSerializer(attachments, many=True).data
        # return LessonAttachmentSerializer(attachments, many=True).data
        # print(serialized_attachments)
        # print("**")
        return {
            'count': len(serialized_attachments),
            'attachments': serialized_attachments
        }

    def get_quiz_questions(self, lesson):
        quiz_questions = Quiz_Question.objects.filter(lesson=lesson)
        quiz_options = QuizOption.objects.filter(name__lesson=lesson)
        serialized_quiz_question = Quiz_QuestionListSerializers(quiz_questions, many=True).data
        serialized_quiz_options = QuizOptionListSerializers(quiz_options, many=True).data
        return {
            'quiz_question': serialized_quiz_question,
            'quiz_options': serialized_quiz_options
        }

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



