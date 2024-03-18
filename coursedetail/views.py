from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import Lesson, Note
from .serializers import LessonCreateSerializers, LessonListSerializers, NoteListSerializers

# Create your views here.

class LessonListView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializers


class LessionRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializers
    

class LessonCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializers
    
class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteListSerializers