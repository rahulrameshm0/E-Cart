from django.db import models
from customers.models import Coustamer
from products.models import Product
# Models for orders.

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    CART_SATGE = 1
    ORDER_CONFIRMED = 1
    OREDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = ((OREDER_PROCESSED,'ORDER_PROCESSED'),(ORDER_DELIVERED,"ORDER_DELIVERED"),(ORDER_REJECTED,"ORDER_REJECTED"))
    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_SATGE)
    total_price = models.FloatField(default=0)
    owner = models.ForeignKey(Coustamer, on_delete=models.SET_NULL,null=True, related_name='orders')
    delete_staus = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "order-{}-{}".format(self.id, self.owner.name)

class OderedItem(models.Model):
    product = models.ForeignKey(Product, related_name='added_carts', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='add_items')

