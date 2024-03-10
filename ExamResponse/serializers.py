from rest_framework import serializers

from Create_Test.models import FullLengthTest, module
from exam.models import Exam, ExamType

from .models import SpeakingResponse, Student_answer, Studentanswer


class StudentAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student_answer
        fields = ("id", "question_number", "answer_text")
        depth = 2

class StudentSpeakingSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpeakingResponse
        fields = ("id", "question_number", "answer_audio")
        depth = 2

    # def get_student_answers(self, obj):
    #     student_answers = Student_answer.objects.filter(student_exam=obj)
    #     return StudentAnswerAnswerSerializers(student_answers, many=True).data


# class StudentAnswerAnswerSerializers(serializers.ModelSerializer):
#     # student_exam = StudentAnswerSerializers(many=True)
#     student_answers = serializers.SerializerMethodField()

#     class Meta:
#         model = Studentanswer
#         # fields = "__all__"
#         fields = ("id", "user", "exam", "student_answers")
#         depth = 2

#     # def create(self, validated_data):
#     #     answers_data = validated_data.pop("student_exam")
#     #     data = super().create(validated_data)
#     #     if answers_data is not None:
#     #         for answer_data in answers_data:
#     #             Student_answer.objects.create(student_answers=data, **answer_data)
#     #     return data

#     def get_student_answers(self, obj):
#         student_answers = Student_answer.objects.filter(student_exam=obj)
#         serialized_answers = StudentAnswerAnswerSerializers(student_answers, many=True).data
#         return serialized_answers


class SpeakingAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakingResponse
        fields = "__all__"


class StudentanswerSerializers(serializers.ModelSerializer):
    student_exam = StudentAnswerSerializers(many=True, required=True)

    class Meta:
        model = Studentanswer
        fields = (
            "id",
            "user",
            "exam",
            "student_exam",
            "AI_Assessment",
            "Tutor_Assessment",
            "band",
        
        )

    def create(self, validated_data):
        student_exam_data = validated_data.pop("student_exam", None)
        studentanswer = Studentanswer.objects.create(**validated_data)
        
        if student_exam_data:
            for answer_data in student_exam_data:
                Student_answer.objects.create(
                    student_answers=studentanswer, **answer_data
                )

        return studentanswer


class StudentanswerSpeakingResponseSerializers(serializers.ModelSerializer):
    student_exams = StudentSpeakingSerializers(many=True, required=True)

    class Meta:
        model = Studentanswer
        fields = (
            "id",
            "user",
            "exam",
            "student_exams",
            "AI_Assessment",
            "Tutor_Assessment",
            "band",
        )

    def create(self, validated_data):
        student_exam_data = validated_data.pop("student_exams", None)
        studentanswer = SpeakingResponse.objects.create(**validated_data)
        
        if student_exam_data:
            for answer_data in student_exam_data:
                SpeakingResponse.objects.create(student_answers=studentanswer, **answer_data)
        return studentanswer
    
from django.contrib.auth.models import User


class StudentExamSerializer(serializers.Serializer):
    exam_id = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all(), required=True)
    data = StudentAnswerSerializers(many=True, required=True)
    


class PracticeTestAnswerSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    Practise_Exam =  serializers.PrimaryKeyRelatedField(queryset=module.objects.all(), required=True)
    answer_data = StudentExamSerializer(many=True, required=True)
        
    def create(self, validated_data):
        answer_data = validated_data.pop('answer_data')
        if answer_data:
            for i in answer_data:
                practice_test_instance  = Studentanswer.objects.create(**validated_data, exam= i['exam_id'])
                for j in i['data']:
                    Student_answer.objects.create(
                        student_answers=practice_test_instance, **j
                        
                    )

        return practice_test_instance


class FLTAnswerSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    Full_Length_Exam =  serializers.PrimaryKeyRelatedField(queryset=FullLengthTest.objects.all(), required=True)
    answer_data = StudentExamSerializer(many=True, required=True)
    exam_type = serializers.ChoiceField(choices = ExamType.choices) #(max_length=40, required=True, )
        
    def create(self, validated_data):
        answer_data = validated_data.pop('answer_data')
        if answer_data:
            for i in answer_data:
                FLT_test_instance  = Studentanswer.objects.create(**validated_data,
                                                                  exam= i['exam_id'],)
                                                                   
                if i['exam_id'].test_type == ExamType.speaking:
                    for j in i['data']:
                        SpeakingResponse.objects.create(
                            student_answers=FLT_test_instance, **j
                            
                        )
                else:                                          
                    for j in i['data']:
                        Student_answer.objects.create(
                            student_answers=FLT_test_instance, **j
                            
                        )

        return FLT_test_instance
    

class PracticeAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = module
        fields = "__all__"
        depth = 2

