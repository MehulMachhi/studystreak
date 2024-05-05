from functools import reduce

from rest_framework import serializers

from exam.serializers import SpeakingPracticeSetSerializer
from utils.dynamic_serializers import DynamicModelSerializer

from .models import FullLengthTest, Responses, createexam, module


class createexamserializers(serializers.ModelSerializer):
    exam_type = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = createexam
        fields = "__all__"
        depth = 2

    def get_exam_type(self, obj):

        listening = obj.IELTS.Listening.exists()
        speaking = obj.IELTS.Speaking.exists()
        writing = obj.IELTS.Writing.exists()
        reading = obj.IELTS.Reading.exists()
        count = reduce(
            lambda x, y: bool(x) + bool(y), [listening, speaking, writing, reading]
        )
        if count >= 2:
            raise serializers.ValidationError(
                "Backend has more than one exam_type, please remove one of them."
            )

        if listening:
            return "Listening"
        elif speaking:
            return "Speaking"
        elif writing:
            return "Writing"
        elif reading:
            return "Reading"
        else:
            return ""


class ResponsesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Responses
        fields = "__all__"
        depth = 2


class ModuleListSerializers(DynamicModelSerializer):
    class Meta:
        model = module
        fields = "__all__"
        depth = 2


class ModuleCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = module
        fields = "__all__"

    def validate(self, attrs):
        count = sum(bool(attrs[key]) for key in ["Listening", "Speaking", "Writing", "Reading"])
        if count > 1:
            raise serializers.ValidationError("Backend has more than one exam_type, please remove and keep one of them.")

        return super().validate(attrs)


class FilterListModuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = module
        fields = "__all__"
        depth = 2

class FLTCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullLengthTest
        fields = "__all__"
        

class FLTserializer(serializers.ModelSerializer):
    speaking_set = SpeakingPracticeSetSerializer()
    class Meta:
        model = FullLengthTest
        fields = "__all__"
        depth = 2

    # def validate(self, attrs):
    #     count = sum(bool(attrs[key]) for key in ["Listening", "Speaking", "Writing", "Reading"])
    #     if count > 1:
    #         raise serializers.ValidationError("Backend has more than one exam_type, please remove and keep one of them.")

    #     return super().validate(attrs)