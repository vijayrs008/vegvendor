"""
URL configuration for VegVendorSys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add',views.add,name='login'),
    path('signup',views.signup,name='user'),
    path('cart',views.cart,name="cart"),
    path('placeorder',views.placeorder,name="placeorder"),
    path('ordered',views.ordered,name="ordered"),
    path('orderdetails',views.orderdetails,name="orderdetails"),
    path('delivered',views.delivered,name="delivered"),
    path('refill',views.refill,name="refill"),
    path('refilled',views.refilled,name="refilled"),
    path('refillsuccess',views.refillsuccess,name="refillsuccess"),
    path('change',views.change,name="change"),
    path('changecost',views.changecost,name="changecost"),
    path('product',views.product,name='product'),
    path('reuser',views.home,name='reuser'),
    path('removecart',views.removecart,name='removecart')
]
