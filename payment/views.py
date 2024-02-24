import json

import razorpay
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .razorpay_api import RazorPayClient
from .serializers import RazorPaySerializer, TransactionSerializer

rz_client = RazorPayClient()
class CreateOrderAPIView(APIView):
    def post(self, request, format=None):
        serializer = RazorPaySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            order_respone = rz_client.create_order(amount=serializer.validated_data['amount'],
                                   currency=serializer.validated_data['currency'])
        
        return Response(order_respone)

class TransactionView(APIView):
    
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            rz_client.verify_payment(razorpay_order_id=serializer.validated_data['order_id'],
                                     razorpay_payment_id=serializer.validated_data['payment_id'],
                                    razorpay_signature=serializer.validated_data['signature'])
            serializer.save()
            return Response({'payment_status':True}, status=200)
@api_view(['POST'])
def start_payment(request):
    # request.data is coming from frontend
    amount = request.data['amount']
    name = request.data['name']

    # setup razorpay client
    client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))

    # create razorpay order
    payment = client.order.create({"amount": int(amount) * 100, 
                                   "currency": "INR", 
                                })

    # we are saving an order with isPaid=False
    order = Order.objects.create(order_product=name, 
                                 order_amount=amount, 
                                 order_payment_id=payment['id'])

    serializer = OrderSerializer(order)

    """order response will be 
    {'id': 17, 
    'order_date': '23 January 2021 03:28 PM', 
    'order_product': '**product name from frontend**', 
    'order_amount': '**product amount from frontend**', 
    'order_payment_id': 'order_G3NhfSWWh5UfjQ', # it will be unique everytime
    'isPaid': False}"""

    data = {
        "payment": payment,
        "order": serializer.data
    }
    return Response(data)


@api_view(['POST'])
def handle_payment_success(request):
    # request.data is coming from frontend
    res = json.loads(request.data["response"])
    print(res)

    """res will be:
    {'razorpay_payment_id':, 
    'razorpay_order_id': 'order_NQHj3dax3AdU5u', 
    'razorpay_signature': ''}
    """
    # ord_id = res.get('razorpay_order_id', '')
    # raz_pay_id = res.get('razorpay_payment_id', '')
    # raz_signature = res.get('razorpay_signature', '')


    ord_id = ""
    raz_pay_id = ""
    raz_signature = ""
    

    # res.keys() will give us list of keys in res
    for key in res.keys():
        if key == 'razorpay_order_id':
            ord_id = res[key]
        elif key == 'razorpay_payment_id':
            raz_pay_id = res[key]
        elif key == 'razorpay_signature':
            raz_signature = res[key]

    # get order by payment_id which we've created earlier with isPaid=False
    order = Order.objects.get(order_payment_id=ord_id)

    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }

    client = razorpay.Client(auth=(config['KEY_ID'], config['KEY_SECRET']))

    # checking if the transaction is valid or not if it is "valid" then check will return None
    check = client.utility.verify_payment_signature(data)

    if check is not None:
        print("Redirect to error url or error page")
        return Response({'error': 'Something went wrong'})

    # if payment is successful that means check is None then we will turn isPaid=True
    order.isPaid = True
    order.save()

    res_data = {
        'message': 'payment successfully received!'
    }

    return Response(res_data)