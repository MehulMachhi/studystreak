from rest_framework import serializers
from .models import Live_Class
from rest_framework import generics

class LiveClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live_Class
        fields = '__all__'
        depth = 2
        
class LiveClassCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live_Class
        fields = "__all__"
        
class LiveClassRetRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        model = Live_Class
        fields = '__all__'
        
        depth = 2
        
    
class LiveClassListWithIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live_Class
        fields = '__all__'
        depth = 2