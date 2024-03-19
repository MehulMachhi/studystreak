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
    serializer_class = NoteListSerializers

    def get_queryset(self):
        queryset = Note.objects.all()
        lesson_id = self.kwargs.get('lesson_id')
        student_id = self.kwargs.get('student_id')

        if student_id:
            queryset = queryset.filter(student_id=student_id)
        if lesson_id:
            queryset = queryset.filter(lesson_id=lesson_id)

        if not (student_id or lesson_id):
            queryset = Note.objects.none()
        return queryset
    

class NoteCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteListSerializers