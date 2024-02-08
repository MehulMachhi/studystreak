from rest_framework import serializers
from .models import Studentanswer, Student_answer


class StudentAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student_answer
        fields = ("id", "question_number", "answer_text")
        depth=2
    # def get_student_answers(self, obj):
    #     student_answers = Student_answer.objects.filter(student_exam=obj)
    #     return StudentAnswerAnswerSerializers(student_answers, many=True).data
class StudentAnswerAnswerSerializers(serializers.ModelSerializer):
    student_exam = StudentAnswerSerializers(many=True)  

    class Meta:
        model = Studentanswer
        fields = "__all__"
        depth = 2

    def create(self, validated_data):
        answers_data = validated_data.pop("student_exam", None)  
        data = super().create(validated_data)
        if answers_data is not None:
            for answer_data in answers_data:
                Student_answer.objects.create(student_answers=data, **answer_data)
        return data


