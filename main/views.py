from calendar import monthrange

from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.models import NewUser
from .models import Income, NecessaryExpenses, DailyExpenses, Category, CategoryIncomes, DailyIncoms, \
    UserCategoryExpenses, UserCategoryIncomes
from datetime import date, datetime
from .forms import DailyExpForm, DailyIncForm, AddIncCategoryForm, AddExpCategoryForm

today = date.today().strftime('%d %B %Y')
category_income = CategoryIncomes
category_exp = Category
def calculate(request):
    title = "Расчет"

    total_inc = Income.objects.filter(user=request.user).aggregate(Sum('sum'))
    total_exp = NecessaryExpenses.objects.filter(user=request.user).aggregate(Sum('sum'))
    try:
        total_save = total_inc['sum__sum'] - total_exp['sum__sum']
    except:
        total_save = 0
    content = {
        "users": NewUser.objects.all(),
        "today": date.today().strftime('%B'),
        "incomes": total_table(Income, request),
        "expenses": total_table(NecessaryExpenses, request),
        "total_expenses": total_exp,
        "total_income": total_inc,
        'total_save': total_save,
        'title': title,
        'simple': for_table_data(total_table(NecessaryExpenses, request))
    }
    return render(request, 'main/calculate.html', content)

def main_page(request):
    title = 'Траты за день'

    dailyexp_form = DailyExpForm(request.POST)
    if request.method == "POST" and dailyexp_form.is_valid():
        DailyExpenses.objects.create(user=request.user, sum=dailyexp_form.cleaned_data['sum'],
                                     category=dailyexp_form.cleaned_data['category'],
                                     description = dailyexp_form.cleaned_data['description'])
        NecessaryExpenses.objects.create(user=request.user, sum=dailyexp_form.cleaned_data['sum'],
                                     category=dailyexp_form.cleaned_data['category'],
                                         description = dailyexp_form.cleaned_data['description'])
        return HttpResponseRedirect(reverse('main'))
    else:
        dailyexp_form = DailyExpForm()
    dailyinc_form = DailyIncForm(request.GET)
    if request.method == "GET" and dailyinc_form.is_valid():
        DailyIncoms.objects.create(user=request.user, sum=dailyinc_form.cleaned_data['sum'],
                                     category=dailyinc_form.cleaned_data['category'],
                                   description = dailyinc_form.cleaned_data['description'])
        Income.objects.create(user=request.user, sum=dailyinc_form.cleaned_data['sum'],
                                     category=dailyinc_form.cleaned_data['category'],
                              description = dailyinc_form.cleaned_data['description'])
        return HttpResponseRedirect(reverse('main'))
    else:
        dailyinc_form = DailyIncForm()

    total_inc=DailyIncoms.objects.filter(user=request.user).aggregate(Sum('sum'))
    total_exp=DailyExpenses.objects.filter(user=request.user).aggregate(Sum('sum'))
    if total_exp['sum__sum'] == None:
        total_exp['sum__sum']=0
    if total_inc['sum__sum'] == None:
        total_inc['sum__sum']=0

    try:
        daily_save = total_inc['sum__sum'] - total_exp['sum__sum']
    except:
        daily_save = 0

    monthly_save = NewUser.objects.get(username=request.user)
    daily_save_amount = monthly_save.monthly_save_amount / monthrange(2024, datetime.now().month)[1]
    content = {'title': title,
               'dailyexp': dailyexp_form,
               'dailyinc': dailyinc_form,
               'today': today,
               'table_daily_exp': total_table(DailyExpenses, request),
               'table_daily_inc':total_table(DailyIncoms, request),
               'total_inc': total_inc,
               'total_exp': total_exp,
               'daily_save': daily_save,
               'daily_save_amount': round(daily_save_amount),
               'weekly_save_amount': round(daily_save_amount)*7,
               'monthly_save_amount': monthly_save.monthly_save_amount,
               'year_save_amount': round(daily_save_amount)*365,
               }
    return render(request, 'main/index.html', content)

def total_table(model, request):
    table_category_summ = {}
    for i in range(category_exp.objects.all().count()):
        res = model.objects.filter(user=request.user, category=i + 1).first()
        res_sum = model.objects.filter(category=i + 1).aggregate(Sum("sum"))
        try:
            table_category_summ[res.category.name] = res_sum['sum__sum']
        except:
            pass
    return table_category_summ

def add_incomes_category(request):
    title = 'Создание категорий'
    if request.method == "POST":
        add_incomes_category_form = AddIncCategoryForm(request.POST)
        if add_incomes_category_form.is_valid():
            UserCategoryIncomes.objects.create(user=request.user, name=add_incomes_category_form.cleaned_data['name'],
                                               description=add_incomes_category_form.cleaned_data['description'])
            return HttpResponseRedirect(reverse('addinccat'))
    else:
        add_incomes_category_form = AddIncCategoryForm()

    content = {'title': title, 'add_incomes_category_form': add_incomes_category_form}
    return render(request, 'main/add_inc_cat.html', content)


def add_expenses_category(request):
    title = 'Создание категорий'
    if request.method == "POST":
        add_expenses_category_form = AddExpCategoryForm(request.POST)
        if add_expenses_category_form.is_valid():
            UserCategoryExpenses.objects.create(user=request.user, name=add_expenses_category_form.cleaned_data['name'],
                                                description=add_expenses_category_form.cleaned_data['description'])
            return HttpResponseRedirect(reverse('addexpcat'))
    else:
        add_expenses_category_form = AddExpCategoryForm()

    content = {'title': title, 'add_expenses_category_form': add_expenses_category_form}
    return render(request, 'main/add_exp_cat.html', content)

def clean_daily_exp_and_inc():
    DailyExpenses.objects.all().delete()
    DailyIncoms.objects.all().delete()

def for_table_data(data):
    result = [['Task', 'Hours per Day'],]
    for i, k in data.items():
        item = []
        item.append(i)
        item.append(k)
        result.append(item)
    return result
