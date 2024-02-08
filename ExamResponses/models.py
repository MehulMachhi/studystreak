from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from exam.models import Exam



class Studentanswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    exam = models.ForeignKey(Exam, related_name="exam", on_delete=models.CASCADE, null=True, blank=True)

class Student_answer(models.Model):
    student_answers = models.ForeignKey(Studentanswer, related_name="student_exam", on_delete=models.CASCADE)
    question_number = (
        models.IntegerField()
    ) 
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text