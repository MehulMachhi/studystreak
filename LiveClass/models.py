from django.db import models
from master.models import batch, Live_Class_Type
from Courses.models import Course 
from django.contrib.auth.models import User
class Live_Class(models.Model):
    select_batch = models.ForeignKey(batch, on_delete=models.CASCADE, null=True, blank=True)
    liveclasstype = models.ForeignKey(Live_Class_Type, on_delete=models.CASCADE, null=True, blank=True)
    meeting_title = models.CharField(max_length=255, null=True, blank=True)
    meeting_description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    zoom_meeting_id = models.CharField(max_length=100, blank=True, null=False)
    zoom_meeting_password = models.CharField(max_length=100, blank=True, null=False)

    def __str__(self):
        return f"{self.meeting_title}"