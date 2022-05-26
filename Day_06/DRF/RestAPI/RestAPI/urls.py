"""RestAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import Calculator.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', Calculator.views.hello, name="hello"),
    path('add/', Calculator.views.calc_add, name="calc_add"),
    path('sub/', Calculator.views.calc_sub, name="calc_sub"),
    path('mul/', Calculator.views.calc_mul, name="calc_mul"),
    path('div/', Calculator.views.calc_div, name="calc_div"),
    path('cls_add/', Calculator.views.class_add.as_view(), name="cls_add"),
]
