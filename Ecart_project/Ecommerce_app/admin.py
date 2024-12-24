from django.contrib import admin

# Register your models here.
from .models import category,product,CartItems,shipping,orders

# Register your models here.
admin.site.register(category)
admin.site.register(product)
admin.site.register(CartItems)
admin.site.register(shipping)
admin.site.register(orders)