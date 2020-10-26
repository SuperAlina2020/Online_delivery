from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'store/home.html')


def products_page(request):
    return render(request,'store/products.html')


def customer_page(request):
    return render(request,'store/customer.html')