from django.shortcuts import render
from .models import HomepageSlider, HomepageSection1, HomepageSection2, Blog
from .serializers import (HomepageSliderRetUpdDelSerializers, HomepageSliderListSerializers, HomepageSection1ListSerializers, 
                          HomepageSection1RetUpdDelSerializers, HomepageSection2ListSerializers, HomepageSection2RetUpdDelSerializers,BlogListSerializers,BlogRetUpdDelSerializers)
from rest_framework import generics
from rest_framework import status


# Create your views here.

    