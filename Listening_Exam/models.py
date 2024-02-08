from django.db import models

# Create your models here.
class ListeningExam(models.Model):
    
    Listening_Exam = models.ManyToManyField("QuestionBank.ReadingQuestion")
      
    def __str__(self):
        return str(self.Listening_Exam)  
    
    