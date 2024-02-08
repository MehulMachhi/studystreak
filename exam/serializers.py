from rest_framework import serializers

from .models import Answer, Exam, FullLengthTest


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "question_number", "answer_text")


class ExamSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Exam
        fields = "__all__"
        depth = 2

    def create(self, validated_data):
        answers_data = validated_data.pop("answers", None)

        data = super().create(validated_data)
        if answers_data is not None:
            for answer_data in answers_data:
                Answer.objects.create(exam=data, **answer_data)

        return data


class FullLengthTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullLengthTest
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["test_type"] = instance.test_type.__str__()
        return data

class ExamListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
        depth = 2


class AnswerListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
        depth = 2

class AnswerRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
        depth = 2


class ExamRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"
        depth=4