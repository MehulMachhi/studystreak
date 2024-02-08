from rest_framework import serializers
from .models import ListeningExam


'''######### ListeningExamListSerializers #########'''

class ListeningExamSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListeningExam
        fields = '__all__'

'''######### ListeningExamRetUpdDelSerializers #########'''

class ListeningExamRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListeningExam
        fields = '__all__'
        