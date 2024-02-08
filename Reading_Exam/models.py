from django.db import models

# Create your models here.
class ReadingExam(models.Model):
    
    Reading_Exam = models.ManyToManyField("QuestionBank.ReadingQuestion")
      
    def __str__(self):
        return str(self.Reading_Exam)    
    