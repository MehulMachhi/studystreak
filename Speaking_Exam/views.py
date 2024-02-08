from django.shortcuts import render
from .models import SpeakingExam
from .serializers import SpeakingExamSerializers,SpeakingExamRetUpdDelSerializers
from rest_framework import generics
from rest_framework import status
# Create your views here.

'''############ SpeakingExamListView ##############'''
    

class SpeakingExamListView(generics.ListCreateAPIView):
    queryset = SpeakingExam.objects.all()
    serializer_class = SpeakingExamSerializers
    
    
'''############ SpeakingExamRetUpdDelViews ##############'''

class SpeakingExamRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpeakingExam.objects.all()
    serializer_class = SpeakingExamRetUpdDelSerializers
    
