from django.db import models
from django.contrib.auth import get_user_model
from products.models import Products
# Create your models here.

User = get_user_model()

ORDER_STATUS_CHOICES = (
    ('created','Created'),
    ('stale', 'Stale'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)

class orders(models.Model):

    user =  models.ForeignKey(User, null= True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Products, null = True, on_delete = models.SET_NULL)

    status = models.CharField(max_length = 20, choices = ORDER_STATUS_CHOICES, default = 'created')

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)

    paid = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)

    shipping_address = models.TextField(blank=True, null = True)
    billing_address = models.TextField(blank=True, null = True)

    timestamp = models.DateTimeField(auto_now_add=True)