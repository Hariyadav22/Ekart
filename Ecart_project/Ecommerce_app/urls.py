from django.urls import path
from . import views
app_name='Ecommerce_app'
urlpatterns = [
    path("",views.home,name='home'),
    path("collections",views.collections,name='collections'),
    path('category/<str:slug>',views.categoryviews,name='categoryviews'),
    path('product/<str:cat_slug>/<str:pro_slug>',views.productviews.as_view(),name="productviews"),
    path("register",views.register,name='register'),
    path("login",views.user_login,name='login'),
    path("logout",views.user_logout,name='logout'),
    path("search",views.search.as_view(),name='search'),

    path('cart/', views.view_cart, name='view_cart'),

    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path("shipping/",views.shipping_data,name='s_details'),
    path("placeorder/",views.place_order,name='placeorder'),
    path("myorders/",views.view_my_orders,name='my_orders'),

]