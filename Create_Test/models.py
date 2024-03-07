from typing import Collection, Iterable

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from exam.models import Difficulty, Exam, ExamType


class Typetest(models.TextChoices):
    practice = "Practice", "Practice"
    full_length = "Full Length", "Full Length"


class module(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Reading = models.ManyToManyField(
        Exam, null=True, blank=True, related_name="reading+"
    )
    Listening = models.ManyToManyField(
        Exam, null=True, blank=True, related_name="listening+"
    )
    Speaking = models.ManyToManyField(
        Exam, null=True, blank=True, related_name="Speaking+"
    )
    Writing = models.ManyToManyField(
        Exam, null=True, blank=True, related_name="writing+"
    )
    exam_test = models.CharField(
        max_length=20, choices=Typetest.choices, null=True, blank=True
    )
    awa = models.ManyToManyField(Exam, null=True, blank=True, related_name="a_w_a+")
    integrated_reasoning = models.ManyToManyField(
        Exam, null=True, blank=True, related_name="integrated_reasoning+"
    )
    quantitative_reasoning = models.ManyToManyField(
        Exam, null=True, blank=True, related_name="quantitative_reasoning+"
    )
    verbal_reasoning = models.ManyToManyField(
        Exam, null=True, blank=True, related_name="verbal_reasoning+"
    )
    difficulty_level = models.CharField(max_length=10, choices = Difficulty.choices, default=Difficulty.easy)
    
    
    def __str__(self):
        return f"{self.Name}"
    


    class Meta:
        verbose_name = "Create Practice Test"
        verbose_name_plural = "Create Practice Tests"
        

class createexam(models.Model):
    IELTS = models.ForeignKey("module", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.IELTS)


class Responses(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=True)
    responses_reading = ArrayField(
        models.SlugField(max_length=500),
        blank=True,
        null=True,
    )
    responses_listening = ArrayField(
        models.SlugField(max_length=500),
        blank=True,
        null=True,
    )
    responses_writing = ArrayField(
        models.SlugField(max_length=500),
        blank=True,
        null=True,
    )
    responses_speaking = models.FileField(
        upload_to="responses_audio/",
        blank=True,
        null=True,
    )


class FullLengthTest(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    reading_set = models.ForeignKey(
        module,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        # limit_choices_to={"Reading__exam_type": ExamType.reading},
        related_name="flt_reading",
    )
    listening_set = models.ForeignKey(
        module,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="flt_listening",
        # limit_choices_to={"Listening__exam_type": ExamType.listening},
    )
    speaking_set = models.ForeignKey(
        module,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="flt_speaking",
        # limit_choices_to={"Speaking__exam_type": ExamType.speaking},
    )
    writing_set = models.ForeignKey(
        module,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="flt_writing",
        # limit_choices_to={"Writing__exam_type": ExamType.writing},
    )
    
    difficulty_level = models.CharField(max_length=20, choices=Difficulty.choices, default=Difficulty.easy)
