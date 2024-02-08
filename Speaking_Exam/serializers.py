from rest_framework import serializers
from .models import SpeakingExam


'''######### SpeakingExamListSerializers #########'''

class SpeakingExamSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpeakingExam
        fields = '__all__'

'''######### SpeakingExamRetUpdDelSerializers #########'''

class SpeakingExamRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpeakingExam
        fields = '__all__'
        