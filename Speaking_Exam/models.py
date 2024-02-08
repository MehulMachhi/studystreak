from django.db import models

# Create your models here.
class SpeakingExam(models.Model):
    
    Speaking_Exam = models.ManyToManyField("QuestionBank.ReadingQuestion")
      
    def __str__(self):
        return str(self.Speaking_Exam)    