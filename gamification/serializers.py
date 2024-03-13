from rest_framework import serializers

from .models import Badge, FlashCard, FlashCardItem, Gamification, PointHistory


class FlashCardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCardItem
        fields = (
            "content",
        )
        extra_kwargs = {
            'flash_card': {'read_only': True}
        }

class FlashCardSerializer(serializers.ModelSerializer):
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
    
class GamificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamification
        fields = '__all__'
        
class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'

class PointHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PointHistory
        fields = '__all__'