from django.shortcuts import render
from .models import WritingExam
from .serializers import WritingExamSerializers, WritingExamRetUpdDelSerializers
from rest_framework import generics
from rest_framework import status
# Create your views here.    
    