from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to='c_images/',null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    

    def __str__(self):
        return self.name

    
class product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to='p_images/',null=True,blank=True)
    small_description=models.CharField(max_length=150,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    description=models.TextField(max_length=150,null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    tag=models.CharField(max_length=150,null=False,blank=False)
    

    def __str__(self):
        return self.name
    

class CartItems(models.Model):
    products = models.ForeignKey(product, on_delete=models.CASCADE,related_name='cartitem')
    quantity = models.PositiveIntegerField(default=0)
    amount=models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    confirm=models.BooleanField(default=False)

    def __str__(self):

        return f'{self.quantity} x {self.products.name}'

    
class shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=False,blank=False)
    email=models.CharField(max_length=100,null=False,blank=False)
    phone=models.CharField(max_length=10,null=False,blank=False)
    address=models.TextField(max_length=150,null=False,blank=False)
    state=models.CharField(max_length=50,null=False,blank=False)
    country=models.CharField(max_length=50,null=False,blank=False)
    pincode=models.IntegerField(null=False,blank=False)
    id_default=models.BooleanField(default=False)
    

    
    def __str__(self):
        return self.state
    
class orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    Shipping=models.ForeignKey(shipping,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.product)

