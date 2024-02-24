from rest_framework import serializers

from .models import Order


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class RazorPaySerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField(max_length=3)
    