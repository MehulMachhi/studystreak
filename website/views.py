from django.shortcuts import render
from .models import HomepageSlider, HomepageSection1, HomepageSection2, Blog
from .serializers import (HomepageSliderRetUpdDelSerializers, HomepageSliderListSerializers, HomepageSection1ListSerializers, 
                          HomepageSection1RetUpdDelSerializers, HomepageSection2ListSerializers, HomepageSection2RetUpdDelSerializers,BlogListSerializers,BlogRetUpdDelSerializers)
from rest_framework import generics
from rest_framework import status


# Create your views here.

'''############ HomepageSliderListView ##############'''

class HomepageSliderListView(generics.ListCreateAPIView):
    queryset = HomepageSlider.objects.all()
    serializer_class = HomepageSliderListSerializers
    
'''############ HomepageSliderRetUpdDelView ##############'''
    
    
class HomepageSliderRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomepageSlider.objects.all()
    serializer_class = HomepageSliderRetUpdDelSerializers
    
'''############ HomepageSection1ListView ##############'''
    
    
class HomepageSection1ListView(generics.ListCreateAPIView):
    queryset = HomepageSection1.objects.all()
    serializer_class = HomepageSection1ListSerializers
    
'''############ HomepageSection1RetUpdDelView ##############'''
 

class HomepageSection1RetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomepageSection1.objects.all()
    serializer_class = HomepageSection1RetUpdDelSerializers
    
'''############ HomepageSection2ListView ##############'''
    

class HomepageSection2ListView(generics.ListCreateAPIView):
    queryset = HomepageSection2.objects.all()
    serializer_class = HomepageSection2ListSerializers
    
'''############ HomepageSection2RetUpdDelViews ##############'''

class HomepageSection2RetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomepageSection2.objects.all()
    serializer_class = HomepageSection2RetUpdDelSerializers


'''############ BlogListView ##############'''
    

class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializers
    
    
'''############ BlogRetUpdDelViews ##############'''

class BlogRetUpdDelViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogRetUpdDelSerializers
    