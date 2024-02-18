from functools import reduce

from rest_framework import serializers

from .models import Responses, createexam, module


class createexamserializers(serializers.ModelSerializer):
    exam_type  = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = createexam
        fields = "__all__"
        depth = 2

    def get_exam_type(self, obj):
        
        listening= obj.IELTS.Listening.exists()
        speaking= obj.IELTS.Speaking.exists()
        writing= obj.IELTS.Writing.exists()
        
        count = reduce(lambda x, y: bool(x) + bool(y), [listening, speaking, writing])
        if count >= 2:
            raise serializers.ValidationError("Backend has more than one exam_type, please remove one of them.")
        
        if listening:
            exam_type = 'Listening'
        elif speaking:
            exam_type = 'Speaking'
        elif writing:
            exam_type = 'Writing'
            
        return exam_type

class ResponsesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Responses
        fields = "__all__"
        depth = 2


class ModuleListSerializers(serializers.ModelSerializer):
    class Meta:
        model = module
        fields = "__all__"
        depth = 2


class ModuleCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = module
        fields = "__all__"
