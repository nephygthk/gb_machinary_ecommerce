from django.db import models
from django.conf import settings

from store.models import Product

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivery in Progress', 'Delivery in Progress'),
        ('Delivered', 'Delivered'),
        ('Stopped by custom', 'Stopped by custom'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='order_user' , null=True)
    email = models.EmailField()
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    Country = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    paid = models.DecimalField(max_digits=9, decimal_places=2)
    balance = models.DecimalField(max_digits=9, decimal_places=2)
    order_key = models.CharField(max_length=200)
    status = models.CharField(max_length=150, choices=STATUS)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return str(self.created)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)