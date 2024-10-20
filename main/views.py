from calendar import monthrange

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import View

from authapp.models import NewUser
from .models import Income, NecessaryExpenses, DailyExpenses, Category, CategoryIncomes, DailyIncoms, \
    FinancialStatement
from datetime import date, datetime, timedelta
from .forms import DailyExpForm, DailyIncForm, AddIncCategoryForm, AddExpCategoryForm, FinancialStatementForm

today = datetime.now().date()

category_income = CategoryIncomes
category_exp = Category
def calculate(request):
    title = "Расчет"
    monthly_save = FinancialStatement.objects.get(user=request.user)
    total_inc = Income.objects.filter(user=request.user).aggregate(Sum('sum'))
    total_exp = NecessaryExpenses.objects.filter(user=request.user).aggregate(Sum('sum'))
    try:
        total_save = total_inc['sum__sum'] - total_exp['sum__sum']
    except:
        total_save = 0
    yestorday = today - timedelta(days=1)
    twodaybefore = today - timedelta(days=2)
    three_day = today - timedelta(days=3)
    four_day = today - timedelta(days=4)
    five_day = today - timedelta(days=5)
    six_day = today - timedelta(days=6)
    inc_two_day = DailyIncoms.objects.filter(user=request.user, time_create__day=twodaybefore.day).aggregate(Sum("sum"))
    if inc_two_day['sum__sum'] == None:
        inc_two_day['sum__sum'] = 0
    exp_two_day = DailyExpenses.objects.filter(user=request.user, time_create__day=twodaybefore.day).aggregate(Sum("sum"))
    if exp_two_day['sum__sum'] == None:
        exp_two_day['sum__sum'] = 0
    inc_three_day = DailyIncoms.objects.filter(user=request.user, time_create__day=three_day.day).aggregate(Sum("sum"))
    if inc_three_day['sum__sum'] == None:
        inc_three_day['sum__sum'] = 0
    exp_three_day = DailyExpenses.objects.filter(user=request.user, time_create__day=three_day.day).aggregate(Sum("sum"))
    if exp_three_day['sum__sum'] == None:
        exp_three_day['sum__sum'] = 0
    inc_four_day = DailyIncoms.objects.filter(user=request.user, time_create__day=three_day.day).aggregate(Sum("sum"))
    if inc_four_day['sum__sum'] == None:
        inc_four_day['sum__sum'] = 0
    exp_four_day = DailyExpenses.objects.filter(user=request.user, time_create__day=three_day.day).aggregate(Sum("sum"))
    if exp_four_day['sum__sum'] == None:
        exp_four_day['sum__sum'] = 0
    inc_five_day = DailyIncoms.objects.filter(user=request.user, time_create__day=three_day.day).aggregate(Sum("sum"))
    if inc_five_day['sum__sum'] == None:
        inc_five_day['sum__sum'] = 0
    exp_five_day = DailyExpenses.objects.filter(user=request.user, time_create__day=three_day.day).aggregate(Sum("sum"))
    if exp_five_day['sum__sum'] == None:
        exp_five_day['sum__sum'] = 0
    inc_six_day = DailyIncoms.objects.filter(user=request.user, time_create__day=three_day.day).aggregate(Sum("sum"))
    if inc_six_day['sum__sum'] == None:
        inc_six_day['sum__sum'] = 0
    exp_six_day = DailyExpenses.objects.filter(user=request.user, time_create__day=three_day.day).aggregate(Sum("sum"))
    if exp_six_day['sum__sum'] == None:
        exp_six_day['sum__sum'] = 0

    content = {
        "users": NewUser.objects.all(),
        "today": today,
        "yestorday": yestorday,
        "twodaybefore": twodaybefore,
        "threedaybefore": three_day,
        "fourdaybefore": four_day,
        "fivedaybefore": five_day,
        "sixdaybefore": six_day,
        "incomes": total_table(Income, request),
        "expenses": total_table(NecessaryExpenses, request),
        "total_expenses": total_exp,
        "total_income": total_inc,
        'total_save': total_save,
        'monthly_save_amount':monthly_save,
        'title': title,
        'simple': for_table_data(total_table(NecessaryExpenses, request)),
        'today_exp': DailyExpenses.objects.filter(user=request.user, time_create__day=datetime.now().day).aggregate(Sum("sum")),
        'today_inc': DailyIncoms.objects.filter(user=request.user, time_create__day=today.day).aggregate(Sum("sum")),
        'yestorday_exp': DailyExpenses.objects.filter(user=request.user, time_create__day=yestorday.day).aggregate(Sum("sum")),
        'yestorday_inc': DailyIncoms.objects.filter(user=request.user, time_create__day=yestorday.day).aggregate(Sum("sum")),
        'twodaybefore_exp': exp_two_day,
        'twodaybefore_inc': inc_two_day,
        'threedaybefore_exp': exp_three_day,
        'threedaybefore_inc': inc_three_day,
        'fourdaybefore_exp': exp_four_day,
        'fourdaybefore_inc': inc_four_day,
        'fivedaybefore_exp': exp_five_day,
        'fivedaybefore_inc': inc_five_day,
        'sixdaybefore_exp': exp_six_day,
        'sixdaybefore_inc': inc_six_day,
    }
    return render(request, 'main/calculate.html', content)

@login_required
def main_page(request):
    title = 'Траты за день'
    user = request.user

    dailyexp_form = DailyExpForm(request.POST, user=user)
    if request.method == "POST" and dailyexp_form.is_valid():
        DailyExpenses.objects.create(user=request.user, sum=dailyexp_form.cleaned_data['sum'],
                                     category=dailyexp_form.cleaned_data['category'],
                                     description = dailyexp_form.cleaned_data['description'])
        NecessaryExpenses.objects.create(user=request.user, sum=dailyexp_form.cleaned_data['sum'],
                                     category=dailyexp_form.cleaned_data['category'],
                                         description = dailyexp_form.cleaned_data['description'])
        return HttpResponseRedirect(reverse('main'))
    else:
        dailyexp_form = DailyExpForm(user=user)

    dailyinc_form = DailyIncForm(request.GET, user=user)
    if request.method == "GET" and dailyinc_form.is_valid():
        DailyIncoms.objects.create(user=request.user, sum=dailyinc_form.cleaned_data['sum'],
                                     category=dailyinc_form.cleaned_data['category'],
                                   description = dailyinc_form.cleaned_data['description'])
        Income.objects.create(user=request.user, sum=dailyinc_form.cleaned_data['sum'],
                                     category=dailyinc_form.cleaned_data['category'],
                              description = dailyinc_form.cleaned_data['description'])
        return HttpResponseRedirect(reverse('main'))
    else:
        dailyinc_form = DailyIncForm(user=user)

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

    monthly_save = FinancialStatement.objects.get(user=request.user)
    daily_save_amount = monthly_save.monthly_target / monthrange(2024, datetime.now().month)[1]
    try:
        degre_save = round(daily_save / round(daily_save_amount) * 100)
    except:
        degre_save = 0
    max_monthly_exp = monthly_save.monthly_incoms-monthly_save.monthly_target

    # statistic_today = DailyExpenses.objects.filter(time_create=today)

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
               'monthly_save_amount': monthly_save,
               'year_save_amount': round(daily_save_amount)*365,
               'max_daily_exp': round(max_monthly_exp/monthrange(2024, datetime.now().month)[1]),
               'degre_exp': round(total_exp['sum__sum']/ round(max_monthly_exp/monthrange(2024, datetime.now().month)[1])*100),
               'degre_save': degre_save,
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
            CategoryIncomes.objects.create(user=request.user, name=add_incomes_category_form.cleaned_data['name'],
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
            Category.objects.create(user=request.user, name=add_expenses_category_form.cleaned_data['name'],
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



class CreateFinStatement(CreateView):
    model = FinancialStatement
    form_class = FinancialStatementForm
    template_name = 'main/fin_statement_create.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        print(self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Финансовая ведомость'

        return context

class EditFinstate(UpdateView):
    model = FinancialStatement
    fields = ['monthly_incoms', 'monthly_expenses', 'monthly_target']
    template_name = 'main/fin_statement_edit.html'
    success_url = reverse_lazy('main')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'финансы/редактирование'
        context['monthly_save_amount'] = FinancialStatement.objects.all()

        return context
