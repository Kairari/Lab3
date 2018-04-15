from django.db import models
from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.email


class Cart(models.Model):
    cart_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_price = models.FloatField()
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def update(self):
        self.last_updated = timezone.now()
        self.save()

    def update_price(self, price):
        self.total_price = price
        self.save()

    def return_paid_carts(self):
        return self.argument_set.filter(paid=True)


    def return_unpaid_carts(self):
        return self.argument_set.filter(paid=False)

    def return_last_updated(self):
        return self.last_updated

    def return_created(self):
        return self.created

    def __str__(self):
        return str(self.cart_code)


class Product(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    carts = models.ManyToManyField(Cart, blank=True)

    def __str__(self):
        return self.name
