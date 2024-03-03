from rest_framework import generics
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from .models import *
from .serializers import (FLTAnswerSerializer, PracticeAnswersSerializer,
                          PracticeTestAnswerSerializer,
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
            return Response({'msg':'created'}, 201)
    
        
class FLTAnswerCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FLTAnswerSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'created'}, 201)
        
from django.shortcuts import get_object_or_404

from Create_Test.models import module
from exam.serializers import AnswerSerializer
from ExamResponse.models import Studentanswer

from .serializers import StudentAnswerSerializers


class PracticeAnswersView(APIView):
    
    def get(self, request, pk):
        try:
            module_instance = module.objects.get(pk=pk)
        except module.DoesNotExist:
            return Response(status=404)
        res_data = {'correct_answers':{},
                    'student_answers':{}}
                    
        practice_instace_data = ['Reading', 'Listening', 'Speaking', 'Writing']
        for i in practice_instace_data:
            for j in getattr(module_instance, i).all():
                serializer = AnswerSerializer(j.answers.all(), many=True)
                
                studentanswer_instance = Studentanswer.objects.filter(Practise_Exam=module_instance,user=request.user, exam = j)
                if (studentanswer_instance.exists()):
                    student_data = StudentAnswerSerializers(studentanswer_instance[0].student_exam.all(), many=True).data
                    if not res_data["student_answers"].get(i, None):
                        res_data['student_answers'][i] = [{'block_id':j.id, "answers":student_data}]
                    else:
                        res_data['student_answers'][i].append({'block_id':j.id, "answers":student_data})
                if not res_data["correct_answers"].get(i, None):
                    res_data['correct_answers'][i] = [{'block_id':j.id, "answers":serializer.data}]
                else:
                    res_data['correct_answers'][i].append({'block_id':j.id, "answers":serializer.data})
                studentanswer_instance
                
        return Response(res_data)