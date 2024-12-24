from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.views import View
# Create your views here.
def home(request):
    cart_count=0
    if request.user.is_authenticated:
        cart_count=CartItems.objects.filter(user=request.user,confirm=False).count()
    else:
        cart_count=0
    return render(request,'EC_app/index.html',{'cart_count':cart_count})

def collections(request):
    categorys=category.objects.filter(status=0)
    cart_count=0
    if request.user.is_authenticated:
        cart_count=CartItems.objects.filter(user=request.user,confirm=False).count()
    return render(request,'EC_app/collections.html',{"category":categorys,'cart_count':cart_count})

from django.db.models import  Q

def categoryviews(request,slug):
    if request.user.is_authenticated:
        if(category.objects.filter(status=0 )):
            products=product.objects.filter(category__slug=slug)
            
            categorys=category.objects.filter(slug=slug).first()
            cart_count=CartItems.objects.filter(user=request.user,confirm=False).count()
            for i in products:
                discount=((i.original_price-i.selling_price)/i.original_price)*100
                saved_amo=i.original_price-i.selling_price
                
                return render(request,'EC_app/categorys/index.html',{'products':products,'categorys':categorys,"discount":discount,"saved_amo":saved_amo,'cart_count':cart_count})
        else:
            messages.warning(request,'no such category found')
            return redirect('collections')
    else:
        messages.success(request,'Your not autherised ! please login')
        return redirect('/collections')
    

class productviews(View):
        def get(self,request,cat_slug,pro_slug):
            if(category.objects.filter(slug=cat_slug ,status=0)):
                if( product.objects.filter(slug=pro_slug,status=0)):
                    viewpro=product.objects.filter(slug=pro_slug,status=0).first()
                else:
                    messages.error(request,'no such product found')
            else:
                messages.warning(request,'no such category found')
                return redirect('collections')
            cart_count=CartItems.objects.filter(user=request.user,confirm=False).count()
           
            return render(request,'EC_app/products/index.html',{"viewpro":viewpro,'cart_count':cart_count})


from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from .forms import signupform
from django.contrib.auth import authenticate ,login ,logout

def register(request):
    if request.method=="POST":
        ur=signupform(request.POST)
        if ur.is_valid():
            uname=ur.cleaned_data ['username']
            upass=ur.cleaned_data ['password1']
            ur.save()
        # messages.success(request,'Registered Successfully ! Login to Continue')
        return redirect('/login')
    else:
        ur=signupform()
    return render(request,'EC_app/athentication/signup.html',{'form':ur})

def user_login(request):
    if request.method=='POST':
        ul=AuthenticationForm(request=request,data=request.POST)

        
        if ul.is_valid():
            uname=ul.cleaned_data['username']
            upass=ul.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Login Successfull !  ')
                return redirect('/collections')
            else:
                messages.success(request,'Invalid Username or Password !  ')
                return redirect('/login')
        
    else:
        ul=AuthenticationForm()
    return render(request,'EC_app/athentication/login.html',{'form':ul})

def user_logout(request):
    if  request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logout Successfully ! ')
    return redirect('/')

from django.views.generic import ListView

class search(ListView):
    model=category
    template_name='EC_app/search.html'
    def get_queryset(self):
            ser = self.request.GET.get('search')
            object_list=category.objects.filter(name__icontains=ser) 
            return object_list

def view_cart(request):
    if  request.user.is_authenticated:
        cart_items = CartItems.objects.filter(user=request.user,confirm=False)
        total_price = sum(item.products.selling_price * item.quantity for item in cart_items)
        cart_count=CartItems.objects.filter(user=request.user,confirm=False).count() 
        ince=request.POST.get('inc')
        dq=request.POST.get('dq')
        l=[]
        for i in cart_items:
            l.append(i.products.name)
            if str(i.products)==str(ince) and i.quantity<i.products.quantity:
                i.quantity+=1
                i.save()


        dec=request.POST.get('dec')
        for i in cart_items:
            if str(i.products)==str(dec) and i.quantity>1:
                i.quantity-=1
                i.save()
        for i in cart_items:
            i.amount=i.quantity*int(i.products.selling_price)
            i.save()

        
        return render(request, 'EC_app/cart.html', {'cart_items': cart_items, 'total_price': total_price,'cart_count':cart_count})
    else:
        messages.success(request,'Your not autherised ! please login')
        return redirect('/collections')
    
def add_to_cart(request, product_id):
    products = product.objects.get(id=product_id)
    cart_item, created = CartItems.objects.get_or_create(products=products, user=request.user,confirm=False)
    
    if cart_item.quantity!=cart_item.products.quantity:
        cart_item.quantity += 1
        cart_item.amount=cart_item.quantity*cart_item.products.selling_price
        cart_item.save()
        if created:
            cart_item.quantity =1
            cart_item.amount=cart_item.quantity*cart_item.products.selling_price
            cart_item.save()
        messages.success(request,f"item add to cart total={cart_item.quantity}")
        url = reverse('Ecommerce_app:productviews', kwargs={'cat_slug': cart_item.products.category.slug,'pro_slug': cart_item.products.slug})
        return redirect(url)
    else:
        messages.success(request,f"catr exide total={cart_item.quantity}")
        url = reverse('Ecommerce_app:productviews', kwargs={'cat_slug': cart_item.products.category.slug,'pro_slug': cart_item.products.slug})
        return redirect(url)
        

def remove_from_cart(request, item_id):
    cart_item = CartItems.objects.get(id=item_id)
    cart_item.delete()
    return redirect('Ecommerce_app:view_cart')

def shipping_data(request):
    if  request.user.is_authenticated:
        l=['Andra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Harryana','Himachal Pradesh','Jarkhand','Karnataka','Kerala','Maharastra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajastan','Sikkim','Tamilnadu','Tripura','Uttarkhand','Uttar Pradesh','West Bengal']
        shipping_items = CartItems.objects.filter(user=request.user,confirm=False)
        Total_amount=sum([int(i.quantity*i.products.original_price) for i in shipping_items])
        
        if request.method=="POST":
            sh=shipping.objects.filter(user=request.user,id_default=True) 
            for i in  sh:
                i.id_default=False
                i.save()
            name=request.POST.get("c_name")
            mail=request.POST.get("c_mail")
            address=request.POST.get("c_address")
            phone=request.POST.get("c_phone")
            state=request.POST.get("c_state")
            pincode=request.POST.get("c_zip")
            s_data=shipping.objects.create(user=request.user,name=name,email=mail,address=address,phone=phone,state=state,pincode=pincode)
            s_data.id_default=True
            s_data.save()
            return redirect('/placeorder/')
        return render(request,'EC_app/shippings.html',{'shipping_items':shipping_items,'states':l,"Total_amount":Total_amount})

def place_order(request):
    ci=CartItems.objects.filter(user=request.user,confirm=False)
    for i in ci:
        created = orders.objects.create(product=i.products,user=request.user,Shipping=shipping.objects.get(user=request.user,id_default=True))
        created.save()
        i.confirm=True
        i.save()
    messages.success(request,'Order Placed Successful')
    return redirect('/')
    
    
    

     
def view_my_orders(request):
    if  request.user.is_authenticated:
        order=orders.objects.filter(user=request.user)
        return render(request, 'EC_app/my_orders.html', {'order_items': order})
    else:
        messages.success(request,'Your not autherised ! please login')
        return redirect('/collections')
    
