from rest_framework import serializers
from .models import ReadingExam


'''######### ReadingExamListSerializers #########'''

class ReadingExamSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReadingExam
        fields = '__all__'

'''######### ReadingExamRetUpdDelSerializers #########'''

class ReadingExamRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReadingExam
        fields = '__all__'
        