from rest_framework import serializers

from Create_Test.models import module
from utils.dynamic_serializers import DynamicModelSerializer

from .models import Answer, Exam, FullLengthTest, SpeakingBlock, SpeakingBlockQuestion


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
        fields = "__all__"
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
        depth = 4


class ExamSerializers(DynamicModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"


class SpeakingBlockQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakingBlockQuestion
        fields = ("speaking_block","question","question_number",)
        extra_kwargs = {"speaking_block": {"write_only": True, "required": False}}


class SpeakingBlockSerializer(serializers.ModelSerializer):
    questions = SpeakingBlockQuestionSerializer(many=True)

    class Meta:
        model = SpeakingBlock
        fields = (
            "id",
            "name",
            "difficulty_level",
            "block_threshold",
            "questions",
            
        )

    def create(self, validated_data):
        questions = validated_data.pop("questions", None)
        speaking_block = super().create(validated_data)

        if questions:
            for question in questions:
                SpeakingBlockQuestion.objects.create(
                    **question, speaking_block=speaking_block
                )

        return speaking_block


class SpeakingPracticeSetSerializer(serializers.ModelSerializer):
    Speaking  = SpeakingBlockSerializer(many=True)
    
    def to_representation(self, instance):
        data =  super().to_representation(instance)
        fields_to_remove =  []
        
        for k, v in data.items():
            if isinstance(v, list) and not v:
                fields_to_remove.append(k)
            elif v is None:
                fields_to_remove.append(k)
        
        for i in fields_to_remove:
            data.pop(i)
        return data
    class Meta:
        fields = '__all__'
        model = module
        