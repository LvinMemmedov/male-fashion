from core.views import * 

from django.urls import path

urlpatterns=[
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("shop/", shop, name="shop"),
    path("about/", about, name="about"),
    path("shop_details/", shop_details, name="shop_details"),
    path("shopping-cart/", shopping_cart, name="shop_cart"),
    path("checkout/", checkout, name="checkout"),
    path("blog_details/",blog_details, name="blog_details"),
    path("blog/", blog, name="blog")

    

  
]