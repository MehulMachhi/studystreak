from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from gamification.models import Gamification
from master.models import Category, ExamType, TestType


class BlockType(models.TextChoices):
    assignments = "Assignments", "Assignments"
    mock_test = "Mock Test", "Mock Test"


class Difficulty(models.TextChoices):
    easy = "Easy", "Easy"
    medium = "Medium", "Medium"
    hard = "Hard", "Hard"


class Category_Type(models.TextChoices):
    IELTS = "IELTS", "IELTS"
    GRE = "GRE", "GRE"
    TOFEL = "TOFEL", "TOFEL"
    GMAT = "GMAT", "GMAT"
    PTE = "PTE", "PTE"
    GENERAL = "GENERAL", "GENERAL"
    DUOLINGO = "DUOLINGO", "DUOLINGO"


class ExamType(models.TextChoices):  # noqa: F811 
    reading = "Reading", "Reading"
    listening = "Listening", "Listening"
    speaking = "Speaking", "Speaking"
    writing = "Writing", "Writing"
    general = "General", "General"
    AWA = "AWA", "AWA"
    integrated_reasoning="Integrated-Reasoning", "Integrated-Reasoning"
    quantitative_reasoning = "Quantitative-Reasoning","Quantitative-Reasoning"
    verbal_reasoning = "Verbal-Reasoning", "Verbal-Reasoning"


# Create your models here.
class Exam(models.Model):
    exam_name = models.CharField(max_length=200, null=True, blank=True)
    exam_type = models.CharField(
        max_length=200,
        choices=ExamType.choices,
        default=ExamType.reading,
        help_text="(Reading, Listening, Speaking, Writing)",
        null=True,
        blank=True,
    )
    # test_type = models.ForeignKey(TestType, on_delete=models.SET_NULL, null=True)
    # question_type = models.ManyToManyField(QuestionType, null=True)
    passage = RichTextUploadingField("contents", null=True, blank=True)
    no_of_questions = models.IntegerField(default=4, null=True, blank=True)
    question = RichTextField(null=True, blank=True)
    block_type = models.CharField(
        max_length=200, choices=BlockType.choices, null=True, blank=True
    )
    difficulty_level = models.CharField(
        max_length=200, choices=Difficulty.choices, null=True, blank=True
    )
    block_threshold = models.PositiveIntegerField(null=True, blank=True)
    type_of_module = models.ForeignKey(
        "master.ModuleType", on_delete=models.SET_NULL, null=True, blank=True
    )
    exam_category = models.CharField(
        max_length=100,
        choices=Category_Type.choices, null=True, blank=True
    )
    audio_file = models.FileField(upload_to="examblockaudio/", null=True, blank=True)
    question_structure = models.JSONField(null=True, blank=True)
    passage_image = models.ImageField(upload_to='passage-images', null=True, blank=True)
    g = GenericRelation(Gamification)

    def __str__(self):
        return f"{self.exam_name}-{self.exam_type}"
    def image_img(self):
        if self.item_image:
            return u'<img src="%s" width="50" height="50" />' % self.item_image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    class Meta:
        verbose_name = "Exam_Block"


class Answer(models.Model):
    exam = models.ForeignKey(Exam, related_name="answers", on_delete=models.CASCADE)
    question_number = (
        models.IntegerField()
    )  # Indicates which question this answer corresponds to
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text

    class Meta:
        unique_together = ("exam", "question_number")


class FullLengthTest(models.Model):
    test_type = models.ForeignKey(
        TestType, on_delete=models.SET_NULL, null=True, help_text="IELTS/PTE etc"
    )
    difficulty_level = models.CharField(max_length=20, choices=Difficulty.choices)
    reading = models.ManyToManyField(
        Exam,
        limit_choices_to={"exam_type": "Reading"},
        related_name="reading",
        null=True,
        blank=True,
    )
    listening = models.ManyToManyField(
        Exam,
        limit_choices_to={"exam_type": "Listening"},
        related_name="listening",
        null=True,
        blank=True,
    )
    writing = models.ManyToManyField(
        Exam,
        limit_choices_to={"exam_type": "Writing"},
        related_name="writing",
        null=True,
        blank=True,
    )
    speaking = models.ManyToManyField(
        Exam, limit_choices_to={"exam_type": "Speaking"}, null=True, blank=True
    )