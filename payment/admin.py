from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_filter = ['user', "product", "amount", "payment_id", "signature_id", "order_id"]
    search_fields = ['user', "product", "amount", "payment_id", "signature_id", "order_id"]
admin.site.register(Order,OrderAdmin)