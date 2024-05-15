
from django.contrib.auth.models import User
from rest_framework import serializers
from Create_Test.models import FullLengthTest, module
from exam.models import Exam, ExamType
from utils.dynamic_serializers import DynamicModelSerializer

from .models import SpeakingBlockAnswer, SpeakingResponse, Student_answer, Studentanswer


class StudentAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student_answer
        fields = ("id", "question_number", "answer_text")
        depth = 2
        extra_kwargs = {
            "answer_text": {"required": False},
        }

class StudentAnswerSerializersDynamic(DynamicModelSerializer):
    class Meta:
        model = Student_answer
        fields = "__all__"
        depth = 2
        extra_kwargs = {
            "answer_text": {"required": False},
        }

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
    student_exam = StudentAnswerSerializers(many=True, required=False)

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
            if validated_data.get("exam").exam_type == ExamType.speaking:
                for answer_data in student_exam_data:
                    SpeakingResponse.objects.create(
                        student_answers=studentanswer,
                        question_number=answer_data.get("question_number",None),
                        answer_text = answer_data.get("answer_text",None),
                    )
            else:
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
                SpeakingResponse.objects.create(
                    student_answers=studentanswer, **answer_data
                )
        return studentanswer




class StudentExamSerializer(serializers.Serializer):
    exam_id = serializers.PrimaryKeyRelatedField(
        queryset=Exam.objects.all(), required=True
    )
    data = StudentAnswerSerializers(many=True, required=True)
    # AI_Assessment = serializers.CharField()
    # band = serializers.CharField()   
    
    # class Meta:
    #     extra_kwargs = {
    #         "AI_Assessment": {"required": False},
    #         "band": {"required": False},
    #     }



class PracticeTestAnswerSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )
    Practise_Exam = serializers.PrimaryKeyRelatedField(
        queryset=module.objects.all(), required=True
    )
    answer_data = StudentExamSerializer(many=True, required=False)

    def create(self, validated_data):
        answer_data = validated_data.pop("answer_data")
        if answer_data:
            for i in answer_data:
                practice_test_instance = Studentanswer.objects.create(
                    **validated_data,
                    exam=i["exam_id"],
                    AI_Assessment = i.get('AI_Assessment',None),
                    band=i.get('band',None)
                )
                if i["exam_id"].exam_type == ExamType.speaking:
                    for j in i["data"]:
                        SpeakingResponse.objects.create(
                            student_answers=practice_test_instance,
                            question_number=j["question_number"],
                            answer_audio=j["answer_text"],
                        )
                else:
                    for j in i["data"]:

                        Student_answer.objects.create(
                            student_answers=practice_test_instance, **j
                        )

        return practice_test_instance


class FLTAnswerSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )
    Full_Length_Exam = serializers.PrimaryKeyRelatedField(
        queryset=FullLengthTest.objects.all(), required=True
    )
    answer_data = StudentExamSerializer(many=True, required=True)
    exam_type = serializers.ChoiceField(
        choices=ExamType.choices
    )  # (max_length=40, required=True, )

    def create(self, validated_data):
        answer_data = validated_data.pop("answer_data")
        if answer_data:
            for i in answer_data:
                FLT_test_instance = Studentanswer.objects.create(
                    **validated_data,
                    exam=i["exam_id"],
                )

                if i["exam_id"].exam_type == ExamType.speaking:
                    for j in i["data"]:
                        SpeakingResponse.objects.create(
                            student_answers=FLT_test_instance,
                            question_number=j["question_number"],
                            answer_audio=j["answer_text"],
                        )
                else:
                    for j in i["data"]:
                        Student_answer.objects.create(
                            student_answers=FLT_test_instance, **j
                        )

        return FLT_test_instance


class PracticeAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = module
        fields = "__all__"
        depth = 2


class SpeakingAnswerBlockSerializer(DynamicModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset= User.objects.all(), write_only=True)
    class Meta:
        model = SpeakingBlockAnswer
        fields = '__all__'
        
    def create(self, validated_data):
        user = validated_data.pop('user',None)
        try:
            student = user.student
        except Exception:
            raise serializers.ValidationError('student does not exists')
        validated_data['user'] = student
        
        return super().create(validated_data)