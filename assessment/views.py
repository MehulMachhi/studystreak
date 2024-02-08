from django.shortcuts import render
from rest_framework import generics
from .serializers import assessmentListSerializer
from .models import assessment

# Create your views here.

class assessmentListView(generics.ListCreateAPIView):
    queryset = assessment.objects.all()
    serializer_class = assessmentListSerializer
        
    
class assessmentRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = assessment.objects.all()
    serializer_class = assessmentListSerializer
    
    

