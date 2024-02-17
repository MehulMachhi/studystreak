from rest_framework import generics

from .serializers import *

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
