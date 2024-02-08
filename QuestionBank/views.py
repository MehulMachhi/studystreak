from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import status
# Create your views here.

'''############ ReadingListView ##############'''
    
class ReadingQuestionListView(generics.ListCreateAPIView):
    queryset = ReadingQuestion.objects.all()
    serializer_class = ReadingQuestionSerializers

class ReadingQuestionTypeNameListView(generics.ListCreateAPIView):
    queryset = ReadingQuestionTypeName.objects.all()
    serializer_class = ReadingQuestionTypeNameSerializers

class ReadingPassageNameListView(generics.ListCreateAPIView):
    queryset = ReadingPassageName.objects.all()
    serializer_class = ReadingPassageNameSerializers

class Reading_QuestionListView(generics.ListCreateAPIView):
    queryset = Reading_Question.objects.all()
    serializer_class = Reading_QuestionSerializers        

class ReadingOptionListView(generics.ListCreateAPIView):
    queryset = ReadingOption.objects.all()
    serializer_class = ReadingOptionSerializers
    
'''############ ReadingRetUpdDelViews ##############'''

class ReadingQuestionRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadingOption.objects.all()
    serializer_class = ReadingOptionRetUpdDelSerializers
    
class ReadingQuestionTypeNameRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadingQuestionTypeName.objects.all()
    serializer_class = ReadingQuestionTypeNameRetUpdDelSerializers

class ReadingPassageNameRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadingPassageName.objects.all()
    serializer_class = ReadingPassageNameRetUpdDelSerializers

class Reading_QuestionRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reading_Question.objects.all()
    serializer_class = Reading_QuestionRetUpdDelSerializers

class ReadingOptionRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadingOption.objects.all()
    serializer_class = ReadingOptionRetUpdDelSerializers


'''############ ListeningListView ##############'''
    
class ListeningQuestionListView(generics.ListCreateAPIView):
    queryset = ListeningQuestion.objects.all()
    serializer_class = ListeningQuestionSerializers

class ListeningQuestionTypeNameListView(generics.ListCreateAPIView):
    queryset = ListeningQuestionTypeName.objects.all()
    serializer_class = ListeningQuestionTypeNameSerializers

class Listening_QuestionListView(generics.ListCreateAPIView):
    queryset = Listening_Question.objects.all()
    serializer_class = Listening_QuestionSerializers

class Listening_OptionsListView(generics.ListCreateAPIView):
    queryset = Listening_Options.objects.all()
    serializer_class = Listening_OptionsSerializers        


'''############ ListeningRetUpdDelViews ##############'''

class ListeningQuestionRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListeningQuestion.objects.all()
    serializer_class = ListeningQuestionRetUpdDelSerializers
    
class ListeningQuestionTypeNameRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListeningQuestionTypeName.objects.all()
    serializer_class = ListeningQuestionTypeNameRetUpdDelSerializers

class Listening_QuestionRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listening_Question.objects.all()
    serializer_class = Listening_QuestionRetUpdDelSerializers

class Listening_OptionsRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listening_Options.objects.all()
    serializer_class = Listening_OptionsRetUpdDelSerializers


'''############ WritingListView ##############'''

class WritingQuestionListView(generics.ListCreateAPIView):
    queryset = WritingQuestion.objects.all()
    serializer_class = WritingQuestionSerializers

class WritingQuestionTypeListView(generics.ListCreateAPIView):
    queryset = WritingQuestionType.objects.all()
    serializer_class = WritingQuestionTypeSerializers        


'''############ WritingRetUpdDelViews ##############'''

class WritingQuestionRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = WritingQuestion.objects.all()
    serializer_class = WritingQuestionRetUpdDelSerializers
    
class WritingQuestionTypeRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = WritingQuestionType.objects.all()
    serializer_class = WritingQuestionTypeRetUpdDelSerializers



'''############ SpeakingListView ##############'''

class SpeakingQuestionListView(generics.ListCreateAPIView):
    queryset = SpeakingQuestion.objects.all()
    serializer_class = SpeakingQuestionSerializers

class SpeakingQuestionTypeListView(generics.ListCreateAPIView):
    queryset = SpeakingQuestionType.objects.all()
    serializer_class = SpeakingQuestionTypeSerializers        


'''############ SpeakingRetUpdDelViews ##############'''

class SpeakingQuestionRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpeakingQuestion.objects.all()
    serializer_class = SpeakingQuestionRetUpdDelSerializers
    
class SpeakingQuestionTypeRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpeakingQuestionType.objects.all()
    serializer_class = SpeakingQuestionTypeRetUpdDelSerializers
