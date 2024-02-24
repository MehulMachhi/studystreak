from rest_framework import status
from rest_framework.serializers import ValidationError

from . import client


class RazorPayClient:
    
    def create_order(self, amount, currency):
        data = {
            "amount": amount * 100,
            "currency": currency,
        }
        try:
            order_data = client.order.create(data=data)
            return order_data
        except Exception as e:
            raise ValidationError({"error": "Razorpay error: " + str(e)})
        
    def verify_payment(self, razorpay_order_id,razorpay_payment_id,razorpay_signature):
        try:
            return client.utility.verify_payment_signature({
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
            })
        except Exception as e:
            raise ValidationError({"error": "Razorpay error: " + str(e)})