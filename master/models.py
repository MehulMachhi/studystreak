# master/models.py
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


class LiveClassType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Catergories"


class Level(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Requirements(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]  # Displaying the first 50 characters

    class Meta:
        verbose_name_plural = "Requirements"


class Outcomes(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]  # Displaying the first 50 characters

    class Meta:
        verbose_name_plural = "Outcomes"


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CourseOverview(models.Model):
    overview = models.TextField()

    def __str__(self):
        return self.overview[:50]  # Displaying the first 50 characters


class SEOMetakeywords(models.Model):
    keywords = ArrayField(models.SlugField(max_length=200), blank=True)

    def __str__(self):
        return " ".join(tag for tag in self.keywords)

    class Meta:
        verbose_name_plural = "SEOMetakeywords"


class PackageType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class Section(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class batch(models.Model):
    batch_name = models.CharField(max_length=200)
    batch_startdate = models.DateField(null=True, blank=True)
    batch_enddate = models.DateField(null=True, blank=True)
    # batch_timing = models.CharField(max_length=200, null=True, blank=True)
    batch_start_timing = models.TimeField(null=True, blank=True)
    batch_end_timing = models.TimeField(null=True, blank=True)
    add_package = models.ForeignKey(
        "package.package", on_delete=models.CASCADE, related_name="+", null=False, blank=True
    )

    def __str__(self):
        return self.batch_name

    class Meta:
        verbose_name_plural = "Batches"


class Attachment(models.Model):
    attachment = models.FileField(
        upload_to="documents/", null=True, blank=True, default=None
    )
    attachment_description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        default=None,
        verbose_name="Attachment Description",
    )

    class Meta:
        abstract = True


class LessonAttachment(Attachment):
    lesson = models.ForeignKey("coursedetail.Lesson", on_delete=models.CASCADE)



class LessonAssignment(Attachment):
    lesson = models.ForeignKey("exam.Exam", on_delete=models.CASCADE)


class CourseMaterial(models.Model):
    material_name = models.CharField(max_length=255)
    course = models.ForeignKey("Courses.Course", on_delete=models.CASCADE)
    course_material = models.FileField(upload_to="course_materials/")

    def __str__(self):
        return self.material_name


class AdditionalResource(models.Model):
    info = models.CharField(max_length=255)
    course = models.ForeignKey("Courses.Course", on_delete=models.CASCADE)
    course_files = models.FileField(upload_to="additional-course-docs/", max_length=100)

    def __str__(self):
        return self.info


class Cupon(models.Model):
    cupon_name = models.CharField(max_length=200, null=True)
    campaign_name = models.CharField(max_length=50)
    cupon_code = models.CharField(max_length=50)
    discount = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.cupon_name 


class ExamType(models.Model):
    exam_type = models.CharField(max_length=100)

    def __str__(self):
        return self.exam_type


class QuestionType(models.Model):
    question_type = models.CharField(max_length=100)

    def __str__(self):
        return self.question_type


class ModuleType(models.Model):
    module_type = models.CharField(max_length=100)

    def __str__(self):
        return self.module_type


class TestType(models.Model):
    """This model is used to store the test type like IELTS, TOEFL, PTE etc."""

    test_type = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.test_type


class Live_Class_Type(models.Model):
    name = models.CharField(max_length = 200 , null=True, blank=True)

    def __str__(self):
        return self.name