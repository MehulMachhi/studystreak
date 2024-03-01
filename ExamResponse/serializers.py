from rest_framework import serializers

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
        print(student_exam_data)
        
        if student_exam_data:
            for answer_data in student_exam_data:
                SpeakingResponse.objects.create(
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

