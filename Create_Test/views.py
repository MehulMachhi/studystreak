from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import createexam, Responses, module
from rest_framework import status
from .serializers import createexamserializers, ResponsesSerializers, ModuleListSerializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.


class createexamview(generics.ListCreateAPIView):
    queryset = createexam.objects.all()
    serializer_class = createexamserializers


class ResponsesView(generics.ListCreateAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializers


class moduleListView(generics.ListCreateAPIView):
    # queryset = module.objects.all()
    # serializer_class = ModuleListSerializers
    def get(self, request, *args, **kwargs):
        exam_test = request.query_params.get('exam_test')
        modules = module.objects.filter(exam_test=exam_test)
        serializer = ModuleListSerializers(modules, many=True)
        return Response(serializer.data)
