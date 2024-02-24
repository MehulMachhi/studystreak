
import razorpay
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    
# data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
# payment = client.order.create(data=data)

# print(payment)