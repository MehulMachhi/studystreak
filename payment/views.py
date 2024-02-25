
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from zoomApi.zoomAPI import ZOomClient

from .razorpay_api import RazorPayClient
from .serializers import RazorPaySerializer, TransactionSerializer

token_url = "https://zoom.us/oauth/token"
base_url = 'https://zoom.us'
Account_id = "hy5Qo6Z-T8-HWmI2vHf4og"
client_id = "qjhZVzGQpq3dMgNyPLdZw"
client_secret = "y4kvGXl0fp64zuSJCQ5dd9ZBNjGlaj8H"xzoomClient = ZOomClient(Account_id, client_id, client_secret)

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
 
class ZoomAPiView(APIView):
    def get(self, request):
        client = zoomClient
        token = client.access_token
        return Response(token)