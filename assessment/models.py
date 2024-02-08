from django.db import models
from Courses.models import Course

# Create your models here.

class assessment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.course)
    
# Create your models here.
