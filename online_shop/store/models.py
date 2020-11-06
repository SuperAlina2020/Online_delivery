from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

class Product(models.Model):
    CATEGORY = (
        ('Телефон','Телефон'),
        ('Компьютер','Компьютер'),
        ('Видеокарта','Видеокарта'),
        ('Жесткий диск','Жесткий диск'),

    )
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    description = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag,null=True)

    def __str__(self):
        return  self.name

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True,blank=True,default='default_image.jpeg')
    github_link = models.CharField(null=True,blank=True,max_length=150)
    insta_link = models.CharField(null=True, blank=True,max_length=150)
    twitter_link = models.CharField(null=True, blank=True,max_length=150)
    facebook_link = models.CharField(null=True, blank=True,max_length=150)

    def __str__(self):
        return self.full_name



class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Not delivered', 'Not delivered'),

    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        return self.product.name







