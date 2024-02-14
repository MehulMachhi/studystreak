from rest_framework import serializers

from .models import Responses, createexam, module


class createexamserializers(serializers.ModelSerializer):
    class Meta:
        model = createexam
        fields = "__all__"
        depth = 2


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
