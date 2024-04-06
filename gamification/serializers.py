from rest_framework import serializers
from utils.dynamic_serializers import DynamicModelSerializer

from .common import MODEL_MAPPER
from .models import Badge, FlashCard, FlashCardItem, Gamification, PointHistory


class FlashCardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCardItem
        fields = (
            "front",
            "back",
        )
        extra_kwargs = {
            'flash_card': {'read_only': True}
        }

class FlashCardSerializer(DynamicModelSerializer):
    flash_card_items = FlashCardItemSerializer(many=True)
    class Meta:
        model = FlashCard
        fields = (
            "id",
            "course",
            "title",
            "description",
            "set_priority",
            "flash_card_items",
            
        )
        depth = 1
        
    def create(self, validated_data):
        flash_card_items = validated_data.pop('flash_card_items')
        flash_card_object = super().create(validated_data)
        
        for item in flash_card_items:
            FlashCardItem.objects.create(flash_card=flash_card_object, **item)
            
        return flash_card_object
    
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model
from django.http import QueryDict


class GamificationCreateSerializer(serializers.Serializer):
    model = serializers.CharField()
    object_id = serializers.IntegerField()
    points = serializers.IntegerField()
    
    
    def __validate_model(self, value):
        if value not in MODEL_MAPPER:
            error_string = f"Invalid model the choices are {', '.join(list(MODEL_MAPPER.keys()))}"
            raise serializers.ValidationError({'model':error_string})
    
    def __validate_object_id(self,value):
        model =MODEL_MAPPER[self.initial_data.get('model')] 
        model_class:Model = ContentType.objects.get_for_model(model).model_class()
        if not model_class.objects.filter(id=value).exists():
            raise serializers.ValidationError({'object_id':'object does not exists'})
        
    def validate(self, attrs):
        self.__validate_model(attrs.get('model'))
        self.__validate_object_id(attrs.get('object_id'))
        return super().validate(attrs)
    
    def create(self, validated_data):
        model_class = MODEL_MAPPER[validated_data['model']]
        content_object = ContentType.objects.get_for_model(model_class)
        object_id = validated_data['object_id']
        points = validated_data['points']
        
        Gamification.objects.create(
            content_type=content_object,
            object_id=object_id,
            points=points
        )
        return validated_data
class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'

class GamificationSerializerForPointHistory(serializers.ModelSerializer):
    class Meta:
        model = Gamification
        fields = "__all__"
class PointHistorySerializer(serializers.ModelSerializer):
    gamification = GamificationSerializerForPointHistory()
    class Meta:
        model = PointHistory
        fields = '__all__'
        
