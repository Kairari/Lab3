from tastypie.resources import ModelResource
from .models import User
from .models import Cart
from .models import Product

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class CartResource(ModelResource):
    class Meta:
        queryset = Cart.objects.all()
        resource_name = 'cart'

class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
