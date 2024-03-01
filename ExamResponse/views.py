from rest_framework import generics
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from .models import *
from .serializers import SpeakingAnswerSerializer, StudentanswerSerializers, StudentanswerSpeakingResponseSerializers


class StudentAnswerListView(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    queryset = Studentanswer.objects.all()
    serializer_class = StudentanswerSerializers


# class SpeakingAnswerListView(generics.ListCreateAPIView):
#     queryset = SpeakingResponse.objects.all()
#     serializer_class = StudentanswerSpeakingResponseSerializers
#     parser_classes = [MultiPartParser, FormParser]
class SpeakingAnswerListView(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    queryset = Studentanswer.objects.all()
    serializer_class = StudentanswerSpeakingResponseSerializers

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)