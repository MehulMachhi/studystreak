from rest_framework import viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

# Create your views here.
from .models import Answer, Exam, FullLengthTest
from .serializers import AnswerSerializer, ExamSerializer, FullLengthTestSerializer, ExamListSerializers, AnswerListSerializers, AnswerRetUpdDelSerializers, ExamRetUpdDelSerializers
from rest_framework import generics 
from django.shortcuts import get_object_or_404
from rest_framework import generics

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def create(self, request, *args, **kwargs):
        # answer_data = request.data.pop("answers")

        return super().create(request, *args, **kwargs)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class FullLengthTestViewSet(viewsets.ModelViewSet):
    queryset = FullLengthTest.objects.all()
    serializer_class = FullLengthTestSerializer

from django_filters.rest_framework import DjangoFilterBackend

class ExamListView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class =  ExamListSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['exam_name'] 



# class AnswerListView(generics.ListAPIView):
#     serializer_class = AnswerListSerializers

#     def get_queryset(self):
#         exam_id = self.kwargs.get('exam_id')
#         exam = get_object_or_404(Exam, id=exam_id)
#         queryset = Answer.objects.filter(exam=exam)
#         return queryset


class ExamListFilterView(generics.ListAPIView):
    serializer_class = ExamListSerializers

    def get_queryset(self):
        block_type = self.request.query_params.get('block_type', None)
        queryset = Exam.objects.all()

        if block_type:
            queryset = queryset.filter(block_type=block_type)

        return queryset


class AnswerListView(generics.ListAPIView):
    serializer_class = AnswerListSerializers
    # queryset = Answer.objects.all()
    print("***")
    # def get_queryset(self):
    #     # exam_id = self.kwargs.get('exam_id')
    #     # queryset = Answer.objects.filter(exam=exam_id)
    #     # exam = get_object_or_404(Exam, id=exam_id)
    #     # queryset = Answer.objects.filter(exam=exam)
    #     exam_id = self.kwargs.get('exam_id')
    #     exam = get_object_or_404(Exam, id=exam_id)
    #     queryset = Answer.objects.filter(exam=exam)
    #     return queryset
    
    # def get_queryset(self):
    #     exam_id = self.kwargs.get('exam_id')
    #     question_number = self.kwargs.get('question_number')
    #     exam = get_object_or_404(Exam, id=exam_id)
    #     queryset = Answer.objects.filter(exam=exam, question_number=question_number)
    
    def get_queryset(self):
        self.exam_id = get_object_or_404(Exam, id=self.kwargs['exam_id'])
        return Answer.objects.filter(exam=self.exam_id)

class AnswerRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerRetUpdDelSerializers


class ExamRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamRetUpdDelSerializers