from django.db import models

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    amount = models.IntegerField()
    payment_id = models.CharField(max_length=100)
    signature_id = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id