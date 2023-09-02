from typing import Any
from django.db import models
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class BaseModel(models.Model):
    created_ad=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    class Meta:
        abstract =True


class New(BaseModel):
    title=models.CharField(max_length=255)
    content=RichTextField()
    image= models.ImageField(upload_to="news",null=True,blank=True)
    like=models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)
    views=models.IntegerField(default=0)
    category=models.CharField(max_length=255)
    

class Product (BaseModel):
    title=models.CharField(max_length=255)
    content=models.TextField()
    image=models.ImageField(upload_to="product",null=True,blank=True)
    price=models.IntegerField(default=0)
    category=models.ForeignKey('Category',on_delete=models.CASCADE, related_name='products')
    slug=models.SlugField(unique=True)
    
    


class Setting(BaseModel):
    logo=models.ImageField(upload_to="logo")
    phone=models.CharField(max_length=255)
    phone2=models.CharField(max_length=255, null=True, blank=True)
    email=models.EmailField()
    text = models.TextField()
    facebook=models.URLField()
    lenkidi=models.URLField()
    instaqram=models.URLField()
    twitter=models.URLField()
    bgimage=models.ImageField()
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=240)

 


class Category(BaseModel):
    title=models.CharField(max_length=255)




class Contact(BaseModel):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=255)
    message=models.TextField()


