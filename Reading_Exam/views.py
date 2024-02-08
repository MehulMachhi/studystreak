from django.shortcuts import render
from .models import ReadingExam
from .serializers import ReadingExamSerializers, ReadingExamRetUpdDelSerializers
from rest_framework import generics
from rest_framework import status
# Create your views here.

'''############ ReadingExamListView ##############'''
    

class ReadingExamListView(generics.ListCreateAPIView):
    queryset = ReadingExam.objects.all()
    serializer_class = ReadingExamSerializers
    
    
'''############ ReadingExamRetUpdDelViews ##############'''

class ReadingExamRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadingExam.objects.all()
    serializer_class = ReadingExamRetUpdDelSerializers
    
