"""
URL configuration for Ecommerce project.

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
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from Ecomapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    # path("home/", views.home, name="home"),
    path("", views.products, name="products"),
    path("catfilter/<cv>", views.catfilter),
    path("sort/<sv>", views.sortprice),
    path("filterbyprice", views.filterbyprice),
    path("product_details/<pid>", views.product_details, name="product"),
    path("viewcart/", views.viewcart, name="viewcart"),
    path("remove/<cid>", views.remove),
    path("updateqty/<x>/<cid>", views.updateqty),
    path("fetchorder/", views.fetchorder),
    path("makepayment/", views.makepayment),
    # path("order_confirmation/", views.order_confirmation, name="order_confirmation"),
    path("paymentsuccess/", views.paymentsuccess),
    path("placeorder/", views.placeorder),
    path("cart/<pid>", views.cart, name="cart"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "E-Kart Admin"
admin.site.site_title = "E-Kart Admin Portal"
admin.site.index_title = "Welcome to E-Kart, your ultimate shopping store"
