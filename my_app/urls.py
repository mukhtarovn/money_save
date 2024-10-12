"""
URL configuration for my_app project.

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
from django.urls import path, include
import main.views as main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.main_page, name='main'),
    path('calculate/', main.calculate, name='calculate'),
    path('add_inc_cat/', main.add_incomes_category, name='addinccat'),
    path('add_exp_cat/', main.add_expenses_category, name='addexpcat'),
    path('auth/', include('authapp.urls', namespace='auth'))
]