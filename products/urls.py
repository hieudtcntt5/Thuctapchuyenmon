
from codecs import namereplace_errors
from django.urls import path,include
from . import views
from products.controller import authview

urlpatterns = [
    path('home',views.home,name="home"),
    path('single',views.single,name="single"),
    path('checkout',views.checkout,name="checkout"),
    path('homecollections/<str:id>',views.homecollections,name='homecollections'),
    path('details_product/<str:id_hangsx>/<str:id_sanpham>',views.details_product,name='details_product'),
    path('register',authview.register,name='register'),
    path('loginpage',authview.loginpage,name='loginpage'),
    path('logoutpage',authview.logoutpage,name='logoutpage'),
    path('searchproduct',views.searchproduct,name="searchproduct"),

    
]
