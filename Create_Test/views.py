# Create your views here.
from rest_framework import generics

from .models import Responses, createexam, module
from .serializers import (
    ModuleCreateSerializers,
    ModuleListSerializers,
    ResponsesSerializers,
    createexamserializers,
)

# Create your views here.


class createexamview(generics.ListCreateAPIView):
    queryset = createexam.objects.all()
    serializer_class = createexamserializers


class ResponsesView(generics.ListCreateAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializers


class moduleListView(generics.ListCreateAPIView):
    queryset = module.objects.all()
    serializer_class = ModuleListSerializers

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ModuleCreateSerializers
        return super().get_serializer_class()
