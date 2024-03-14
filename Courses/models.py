# Courses/models.py

from ckeditor.fields import RichTextField
from django.contrib.auth.models import Group, User
from django.contrib.postgres.fields import ArrayField
from django.db import models

from coursedetail.models import Lesson
from master.models import Category, Language, Level, Outcomes, Requirements


class course_type(models.TextChoices):
    private = "PRIVATE", "PRIVATE"
    public = "PUBLIC", "PUBLIC"


class course_delivery(models.TextChoices):
    taught = "TAUGHT", "Taught course"
    self_study = "SELF-STUDY", "Self-study course"


class Course(models.Model):
    # Course Detail
    Course_Title = models.CharField(max_length=200)
    Short_Description = RichTextField()
    Description = (
        RichTextField()
    ) 
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Level = models.ForeignKey(Level, on_delete=models.CASCADE)
    Language = models.ForeignKey(Language, on_delete=models.CASCADE)
    EnrollmentStartDate = models.DateField()
    EnrollmentEndDate = models.DateField()
    max_enrollments = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    faqs = RichTextField()
    Featured = models.BooleanField(default=False)
    Support_Available = models.BooleanField(default=False)

    Requirements = models.ManyToManyField(Requirements)

    Outcome = models.ManyToManyField(Outcomes)

    # Course Media
    Course_Overview_Provider = models.CharField(max_length=200, null=True, blank=True,)
    Course_Overview_URL = models.URLField(null=True, blank=True,)
    Course_Thumbnail = models.ImageField(upload_to="course_thumbnails/")
    # Course SEO
    SEO_Meta_Keywords = ArrayField(models.SlugField(max_length=200), blank=True)
    Meta_Description = ArrayField(models.SlugField(max_length=200), blank=True)
    # Lessons
    lessons = models.ManyToManyField(Lesson, blank=True)

    course_delivery = models.CharField(
        max_length=200, null=True, blank=True, choices=course_delivery.choices
    )
    course_type = models.CharField(
        max_length=200, null=True, blank=True, choices=course_type.choices
    )

    primary_instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True, limit_choices_to={'groups__name': 'Instructor'})
    course_identifier = models.CharField(
        max_length=200, null=True, blank=True, unique=True
    )
    tutor = models.ManyToManyField(User, related_name="tutor", null=False,blank=True, limit_choices_to={'groups__name': 'Tutor'})

    def __str__(self):
        return self.Course_Title

class YoutubeDataRecord(models.Model):
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.CharField()
    lesson = models.ForeignKey("coursedetail.Lesson", on_delete=models.CASCADE, related_name = 'youtube_data', null=True, blank=True)
    
    class Meta:
        db_table = 'youtubeDataRecord'
        