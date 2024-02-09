from .serializers import *
from rest_framework import generics
from .models import Student_answer
from rest_framework import viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser


# class StudentAnswerListView(generics.ListCreateAPIView):
#     # queryset = StudentAnswer
#     queryset = Studentanswer.objects.all()
#     serializer_class = StudentAnswerAnswerSerializers
#     parser_classes = [MultiPartParser, FormParser, JSONParser]

#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

class StudentAnswerListView(generics.ListCreateAPIView):
    queryset = Studentanswer.objects.all()
    serializer_class = StudentanswerSerializers