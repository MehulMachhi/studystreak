from django.shortcuts import render
from .models import ListeningExam
from .serializers import ListeningExamSerializers, ListeningExamRetUpdDelSerializers
from rest_framework import generics
from rest_framework import status
# Create your views here.
'''############ ListeningExamView ##############'''
    

class ListeningExamListView(generics.ListCreateAPIView):
    queryset = ListeningExam.objects.all()
    serializer_class = ListeningExamSerializers
    
    
'''############ ListeningExamRetUpdDelViews ##############'''

class ListeningExamRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListeningExam.objects.all()
    serializer_class = ListeningExamRetUpdDelSerializers
    
