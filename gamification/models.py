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
    flash_card = models.ForeignKey(FlashCard, on_delete=models.CASCADE, related_name="flash_card_items")
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
    
    def __str__(self):
        return f"{self.content_type.name}-{self.content_object.__str__()}"
        
class Badge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    points_required = models.PositiveIntegerField(default=0)
    gamification_items = models.ManyToManyField(Gamification)
    next_badge = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title}-{self.points_required}"
    
    
class PointHistory(models.Model):
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    gamification = models.ForeignKey(Gamification, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.get_name()
    
    class Meta:
        verbose_name_plural = "Point Histories"