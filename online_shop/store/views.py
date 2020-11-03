from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from .forms import OrderForm
from .filters import OrderFilterSet
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegisterForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .decorators import *


@unauth_user
def register(request):
    form = CustomRegisterForm()
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You auth successfully')
            return redirect('home')
    context = {'form':form}
    return render(request,'store/register.html',context)


def user_page(request):
    orders = request.user.customer.order_set.all()
    context = {'orders':orders}
    return render(request,'store/user.html',context)

@unauth_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        login(request, user)
        return redirect('home')
    context = {}
    return render(request,'store/login.html',context)


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home_page(request):
    customers = Customer.objects.all()
    delivered = Order.objects.filter(status='Delivered').count()
    orders = Order.objects.all()
    orders_count = Order.objects.all().count()
    pending = Order.objects.filter(status='Pending').count()
    not_delivered = Order.objects.filter(status='Not delivered').count()
    context = {'customers':customers,'orders':orders,'orders_count':orders_count,'delivered':delivered,'pending':pending,'not_delivered':not_delivered}
    return render(request,'store/home.html',context)



def products_page(request):
    products = Product.objects.all()
    context = {'products':products}

    return render(request,'store/products.html',context)


@admin_only
def customer_page(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
        orders = customer.order_set.all()
        orders_count = orders.count()
        filterset = OrderFilterSet(request.GET,queryset=orders)
        orders = filterset.qs # Обращаемся к классу Model
        context = {'customer':customer,'orders':orders,'orders_count':orders_count,'filterset':filterset}
        return render(request,'store/customer.html',context)

    except ObjectDoesNotExist:
        return HttpResponse('Takogo net')

def create_order(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset,'customer':customer}
    return render(request,'store/order_form.html',context)

def update_order(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'store/order_form.html',context)

def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'order':order}
    return render(request,'store/delete.html',context)