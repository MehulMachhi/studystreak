from rest_framework import generics
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from Create_Test.models import FullLengthTest
from .models import *
from .serializers import (FLTAnswerSerializer, PracticeAnswersSerializer,
                          PracticeTestAnswerSerializer,
                          SpeakingAnswerSerializer, StudentanswerSerializers,
                          StudentanswerSpeakingResponseSerializers,
                          StudentExamSerializer)

def get_answers(self, practice_set_instance):
        res_data = {'correct_answers':{},
                    'student_answers':{}}
                    
        practice_instance_data = ['Reading', 'Listening', 'Speaking', 'Writing']
        for i in practice_instance_data:
    
            for j in getattr(practice_set_instance, i).all():
                serializer = AnswerSerializer(j.answers.all(), many=True)
                if res_data['correct_answers'].get(i,None):
                    res_data['correct_answers'][i].append({'block_id':j.id, "answers":serializer.data})
                else:
                    res_data['correct_answers'][i] = [{'block_id':j.id, "answers":serializer.data}]

                studentanswer_instance = Studentanswer.objects.filter(Practise_Exam=practice_set_instance,user=self.request.user, exam = j).first()
                if (studentanswer_instance):
                    student_data = StudentAnswerSerializers(studentanswer_instance.student_exam.all(), many=True).data
                    if res_data['student_answers'].get(i,None):
                        res_data['student_answers'][i].append({'block_id':j.id, "answers":student_data})
                    else:
                        res_data['student_answers'][i] = [{'block_id':j.id, "answers":student_data}]


        return res_data
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

        res_data = get_answers(self,module_instance)
        res_data["name"] = module_instance.Name
        res_data["difficulty_level"] = module_instance.difficulty_level
        return Response(res_data)
    


class FLTAnswers(APIView):
    def get(self, request, flt_id):
        try:
            flt_instance = FullLengthTest.objects.get(pk=flt_id)
        except FullLengthTest.DoesNotExist:
            return Response('record with this id does not exists',400)
        

        reading_set_data = get_answers(self,flt_instance.reading_set)
        speaking_set_data = get_answers(self,flt_instance.speaking_set)
        writing_set_data = get_answers(self,flt_instance.writing_set)
        listening_set_data = get_answers(self,flt_instance.listening_set)

        return Response({
            "reading_set":reading_set_data,
            "speaking_set":speaking_set_data,
            "writing_set":writing_set_data,
            "listening_set":listening_set_data,
        }, 200)
    
        # return Response(
        #     [
        #         reading_set_data,
        #         speaking_set_data,
        #         writing_set_data,
        #         listening_set_data,

        #     ],
        #     200
        # )

        
class FLTAnswerCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FLTAnswerSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'created'}, 201)