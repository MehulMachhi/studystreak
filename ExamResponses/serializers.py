from rest_framework import serializers
from .models import Studentanswer, Student_answer

class StudentAnswerAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Studentanswer
        # fields = ("question_number", "answer_text")
        fields = "__all__"


class StudentAnswerSerializers(serializers.ModelSerializer):
    student_answers = serializers.SerializerMethodField()
    class Meta:
        model = Studentanswer
        fields = "__all__"
        depth=2

    def get_student_answers(self, obj):
        student_answers = Student_answer.objects.filter(student_exam=obj)
        return StudentAnswerAnswerSerializers(student_answers, many=True).data