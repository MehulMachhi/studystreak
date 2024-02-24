
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .razorpay_api import RazorPayClient
from .serializers import RazorPaySerializer, TransactionSerializer

rz_client = RazorPayClient()
class CreateOrderAPIView(APIView):
    def post(self, request, format=None):
        serializer = RazorPaySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            order_respone = rz_client.create_order(amount=serializer.validated_data['amount'],
                                   currency=serializer.validated_data['currency'])
        
        return Response(order_respone, status=status.HTTP_201_CREATED)

class TransactionView(APIView):
    
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            rz_client.verify_payment(razorpay_order_id=serializer.validated_data['order_id'],
                                     razorpay_payment_id=serializer.validated_data['payment_id'],
                                    razorpay_signature=serializer.validated_data['signature'])
            serializer.save()
            return Response({'payment_status':True}, status=200)
 