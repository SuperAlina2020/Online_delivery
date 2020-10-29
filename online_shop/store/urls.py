from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home_page,name='home'),
    path('register/',register,name='register'),
    path('products/',products_page,name='products'),
    path('customer/<int:pk>/',customer_page,name='customer'),
    path('create_order/<int:pk>/',create_order,name='create_order'),
    path('update_order/<int:pk>/',update_order,name='update_order'),
    path('delete_order/<int:pk>/',delete_order,name='delete_order'),


]
