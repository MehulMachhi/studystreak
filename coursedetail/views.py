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
        student_id = self.request.query_params.get('student_id')
        lesson_id = self.request.query_params.get('lesson_id')

        if student_id:
            queryset = queryset.filter(student_id=student_id)
        if lesson_id:
            queryset = queryset.filter(lesson_id=lesson_id)
            print(queryset)
        return queryset