from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from Courses.models import Course

# Create your models here.

class FlashCard(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField()
    description = models.TextField()
    set_priority = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=[
                "course",
                "set_priority"],
                name="unique_flashcard_title",
                violation_error_message="Can not set same priority for same course")
        ]
    def __str__(self):
        return self.title
    
class FlashCardItem(models.Model):
    flash_card = models.ForeignKey(FlashCard, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    def __str__(self):
        return self.content
    
class Gamification(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    points = models.PositiveIntegerField(default=1)

     