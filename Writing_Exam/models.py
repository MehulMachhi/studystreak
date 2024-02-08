from django.db import models

# Create your models here.

class WritingExam(models.Model):
    
    Writing_Exam = models.ManyToManyField("QuestionBank.ReadingQuestion")
      
    def __str__(self):
        return str(self.Writing_Exam)  