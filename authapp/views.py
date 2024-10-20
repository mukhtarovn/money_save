from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView

from authapp.forms import NewUserLoginForm, NewUserRegisterForm, NewUserEditForm
from django.contrib import auth
from django.urls import reverse

from main.models import Category, CategoryIncomes


def login(request):
    title = 'вход'

    login_form = NewUserLoginForm(data=request.POST)
    if request.method == 'POST':
        username = request.POST ['username']
        password = request.POST ['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('auth:login'))

def register(request):
    title = 'регистрация'
    if request.method == "POST":
        register_form = NewUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                create_category(request)
                return HttpResponseRedirect(reverse('finstat'))
    else:
        register_form = NewUserRegisterForm()


    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)

def edit(request):
    title = 'редактирование'
    if request.method == "POST":
        edit_form = NewUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        edit_form = NewUserEditForm(instance=request.user)
    content = {'title': title,'edit_form': edit_form}


    return render(request,'authapp/edit.html', content)


class UserCategoryIncomes(object):
    pass


def create_category(request):
    Category.objects.bulk_create([
        Category(user=request.user, name='АРЕНДА'),
        Category(user=request.user, name='ИПОТЕКА'),
        Category(user=request.user, name='КРЕДИТЫ'),
        Category(user=request.user, name='КОМУНАЛЬНЫЕ ПЛАТЕЖИ'),
        Category(user=request.user, name='ТЕЛЕФОНЫ/СВЯЗЬ'),
        Category(user=request.user, name='КАФЕ/РЕСТОРАНЫ'),
        Category(user=request.user, name='ПРОДУКТЫ ПИТАНИЯ'),
    ])
    CategoryIncomes.objects.bulk_create([
        CategoryIncomes(user=request.user, name='ЗАРПЛАТА'),
        CategoryIncomes(user=request.user, name='ДОПОЛНИТЕЛЬНЫЙ ДОХОД'),
    ])