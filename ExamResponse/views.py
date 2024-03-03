from rest_framework import generics
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from .models import *
from .serializers import (PracticeTestAnswerSerializer,
                          SpeakingAnswerSerializer, StudentanswerSerializers,
                          StudentanswerSpeakingResponseSerializers,
                          StudentExamSerializer)


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
    
from rest_framework.response import Response
from rest_framework.views import APIView


class PracticeTestAnswerCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PracticeTestAnswerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()  
            return Response(None, 200)