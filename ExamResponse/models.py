from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Test
from exam.models import Exam


class Studentanswer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    exam = models.ForeignKey(Exam, related_name="exam", on_delete=models.CASCADE)
    band = models.CharField(null=True, blank=True)
    gpt_response = models.TextField(null=True, blank=True)

class Student_answer(models.Model):
    student_answers = models.ForeignKey(
        Studentanswer, related_name="student_exam", on_delete=models.CASCADE
    )
    question_number = models.IntegerField()
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text


class SpeakingResponse(models.Model):
    student_answers = models.ForeignKey(Studentanswer, on_delete=models.CASCADE)
    question_number = models.IntegerField()
    answer_audio = models.FileField()
