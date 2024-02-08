from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
### Reading ###
class ReadingOption(models.Model):
    name = models.ForeignKey('Reading_Question', on_delete= models.CASCADE)
    Answers = models.CharField(max_length=200, null=True, blank=True) 
    Corect_Answer = models.BooleanField(default=False)
    def __str__(self):
        return str(self.Answers)  



class Reading_Question(models.Model):
    Question = models.CharField(max_length=200, null=True, blank=True) 
    name = models.ForeignKey('QuestionBank.ReadingQuestion', on_delete= models.CASCADE)
    def __str__(self):
        return str(self.name)    
    
class ReadingPassageName(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    def __str__(self):
        return str(self.title)    

class ReadingQuestionTypeName(models.Model):
    TypeName = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.TypeName)
    
class ReadingQuestion(models.Model):
    passage = models.ForeignKey(ReadingPassageName, on_delete=models.CASCADE)
    question_type = models.ForeignKey(ReadingQuestionTypeName, on_delete=models.CASCADE)
    Instructions = RichTextField()
    def __str__(self):
        return f"{self.passage} - {self.question_type} - {self.Instructions}"
    
    
'''############ Listening ##############'''    

class Listening_Options(models.Model):
    Answer = models.CharField(max_length=200, null=True, blank=True) 
    Correct_Answer = models.BooleanField(default=False)
    name = models.ForeignKey('Listening_Question', on_delete= models.CASCADE)

class Listening_Question(models.Model):
    Question = models.CharField(max_length=200, null=True, blank=True) 
    name = models.ForeignKey('QuestionBank.ListeningQuestion', on_delete= models.CASCADE)
    def __str__(self):
        return str(self.Question)  

class ListeningQuestionTypeName(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)

class ListeningQuestion(models.Model):
    Audio = models.FileField(upload_to='audio/')
    question_type = models.ForeignKey(ListeningQuestionTypeName, on_delete=models.CASCADE)
    Instructions = RichTextField()
    def __str__(self):
        return f"{self.Audio} - {self.question_type} - {self.Instructions}"
    
    
'''############ Writing ##############'''    

class WritingQuestionType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return str(self.name)

class WritingQuestion(models.Model):
    question_type = models.ForeignKey(WritingQuestionType, on_delete=models.CASCADE)
    Instructions = RichTextField()
    # passage = models.ForeignKey(LPassageName, on_delete=models.CASCADE, null=True, blank=True)
    Ans = RichTextField()
    
    def __str__(self):
        return f"{self.question_type} - {self.Instructions}"    
    
'''############ Speaking ##############'''

class SpeakingQuestionType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)

class SpeakingQuestion(models.Model):
    question_type = models.ForeignKey(SpeakingQuestionType, on_delete=models.CASCADE)
    Audio = models.FileField(upload_to='audio/')
    Instructions = RichTextField()
    # passage = models.ForeignKey(LPassageName, on_delete=models.CASCADE, null=True, blank=True)
    Ans = RichTextField()
    
    def __str__(self):
        return f"{self.question_type}"    
    