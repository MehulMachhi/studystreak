from rest_framework import serializers
from .models import assessment
from django.contrib.auth.models import User

class assessmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = assessment
        fields = '__all__'
        
        depth = 2
        
        
class assessmentRetUpdDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = assessment
        fields = '__all__'
        
        depth = 2
        

