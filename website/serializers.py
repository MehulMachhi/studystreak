from rest_framework import serializers
from .models import HomepageSlider, HomepageSection1, HomepageSection2, Blog

'''######### HomepageSliderListSerializers #########'''

class HomepageSliderListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomepageSlider
        fields = '__all__'
        
'''######### HomepageSliderRetUpdDelSerializers #########'''
        
class HomepageSliderRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomepageSlider
        fields = '__all__' 
        
'''######### HomepageSection1ListSerializers #########'''
           

class HomepageSection1ListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomepageSection1
        fields = '__all__'
        
'''######### HomepageSection1RetUpdDelSerializers #########'''
        

class HomepageSection1RetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomepageSection1
        fields = '__all__'
        
'''######### HomepageSection2ListSerializers #########'''
        
class HomepageSection2ListSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomepageSection2
        fields = '__all__'

'''######### HomepageSection2RetUpdDelSerializers #########'''
        
class HomepageSection2RetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomepageSection2
        fields = '__all__'
    
'''######### BlogListSerializers #########'''

class BlogListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

'''######### BlogRetUpdDelSerializers #########'''

class BlogRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        