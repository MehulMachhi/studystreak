from rest_framework import generics
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from .serializers import *

# class StudentAnswerListView(generics.ListCreateAPIView):
#     # queryset = StudentAnswer
#     queryset = Studentanswer.objects.all()
#     serializer_class = StudentAnswerAnswerSerializers
#     parser_classes = [MultiPartParser, FormParser, JSONParser]

#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)


class StudentAnswerListView(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    queryset = Studentanswer.objects.all()
    serializer_class = StudentanswerSerializers

    def create(self, request, *args, **kwargs):
        print(type(request.data))
        return super().create(request, *args, **kwargs)
