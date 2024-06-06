from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from Create_Test.models import createexam, module

from .models import Answer, Exam, FullLengthTest, SpeakingBlock
from .serializers import (
    AnswerListSerializers,
    AnswerRetUpdDelSerializers,
    AnswerSerializer,
    CreateExamSerializer,
    ExamListSerializers,
    ExamRetUpdDelSerializers,
    ExamSerializer,
    FullLengthTestSerializer,
    SpeakingBlockSerializer,
    
)


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


# class FullLengthTestViewSet(viewsets.ModelViewSet):
#     queryset = FullLengthTest.objects.all()
#     serializer_class = FullLengthTestSerializer


#     serializer_class = FullLengthTestSerializer





# class AnswerListView(generics.ListAPIView):
#     serializer_class = AnswerListSerializers

#     def get_queryset(self):
#         exam_id = self.kwargs.get('exam_id')
#         exam = get_object_or_404(Exam, id=exam_id)
#         queryset = Answer.objects.filter(exam=exam)
#         return queryset




# class AnswerListView(generics.ListAPIView):
#     serializer_class = AnswerListSerializers
    # queryset = Answer.objects.all()
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
    
    # def get_queryset(self):
    #     self.exam_id = get_object_or_404(Exam, id=self.kwargs['exam_id'])
    #     return Answer.objects.filter(exam=self.exam_id)



class SpeakingBlockView(generics.ListCreateAPIView):
    serializer_class = SpeakingBlockSerializer
    queryset = SpeakingBlock.objects.all()
    

class SpeakingBlockRetrieveView(generics.RetrieveAPIView):
    serializer_class = SpeakingBlockSerializer
    queryset = SpeakingBlock.objects.all()
    
class SpeakingPracticeSetView(generics.RetrieveAPIView):
    serializer_class=  CreateExamSerializer
    queryset = createexam.objects.all()