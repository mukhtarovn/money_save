
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import main.views as main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.main_page, name='main'),
    path('calculate/', main.calculate, name='calculate'),
    path('add_inc_cat/', main.add_incomes_category, name='addinccat'),
    path('add_exp_cat/', main.add_expenses_category, name='addexpcat'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('fin_statement/', main.CreateFinStatement.as_view(), name="finstat"),
    path('fin_statement_edit/<pk>', main.EditFinstate.as_view(), name="finstatedit"),
    path('category_list/', main.UserCategory.as_view(), name="category_list"),
    path('category_del/<int:pk>', main.user_category_delete , name="category_delete"),
    path('inccategory_del/<int:pk>', main.user_income_category_delete , name="income_category_delete"),
]