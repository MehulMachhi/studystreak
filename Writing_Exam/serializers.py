from rest_framework import serializers
from .models import WritingExam





'''######### WritingExamListSerializers #########'''

class WritingExamSerializers(serializers.ModelSerializer):
    class Meta:
        model = WritingExam
        fields = '__all__'

'''######### WritingExamRetUpdDelSerializers #########'''

class WritingExamRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = WritingExam
        fields = '__all__'
        