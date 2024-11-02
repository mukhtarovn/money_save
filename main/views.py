from calendar import monthrange

from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from authapp.models import NewUser
from .models import Income, NecessaryExpenses, Category, CategoryIncomes, \
    FinancialStatement
from datetime import datetime, timedelta
from .forms import DailyExpForm, DailyIncForm, AddIncCategoryForm, AddExpCategoryForm, FinancialStatementForm

today = datetime.now().date()

category_income = CategoryIncomes
category_exp = Category

def save_time(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_time = data.get('user_time', None)
        if user_time:
            # Обрабатывайте полученное время, сохраняйте в базе данных или выполняйте другие действия
            print(f"Время пользователя: {user_time[0:2]}")
            today = user_time[0:2]
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def calculate(request):
    title = "Расчет"
    monthly_save = FinancialStatement.objects.get(user=request.user)
    total_inc = Income.objects.filter(user=request.user).aggregate(Sum('sum'))
    total_exp = NecessaryExpenses.objects.filter(user=request.user).aggregate(Sum('sum'))
    try:
        total_save = total_inc['sum__sum'] - total_exp['sum__sum']
    except:
        total_save = 0
    yestorday = today - timedelta(days=31)
    twodaybefore = today - timedelta(days=60)
    three_day = today - timedelta(days=90)
    four_day = today - timedelta(days=120)
    five_day = today - timedelta(days=150)
    six_day = today - timedelta(days=180)

    inc_today = Income.objects.filter(user=request.user, time_create__month=today.month).aggregate(Sum("sum"))
    if inc_today['sum__sum'] == None:
        inc_today['sum__sum'] = 0
    exp_today = NecessaryExpenses.objects.filter(user=request.user, time_create__month=today.month).aggregate(
        Sum("sum"))
    if exp_today['sum__sum'] == None:
        exp_today['sum__sum'] = 0
    inc_yesterday = Income.objects.filter(user=request.user, time_create__month=yestorday.month).aggregate(Sum("sum"))
    if inc_yesterday['sum__sum'] == None:
        inc_yesterday['sum__sum'] = 0
    exp_yesterday = NecessaryExpenses.objects.filter(user=request.user, time_create__month=yestorday.month).aggregate(
        Sum("sum"))
    if exp_yesterday['sum__sum'] == None:
        exp_yesterday['sum__sum'] = 0
    inc_two_day = Income.objects.filter(user=request.user, time_create__month=twodaybefore.month).aggregate(Sum("sum"))
    if inc_two_day['sum__sum'] == None:
        inc_two_day['sum__sum'] = 0
    exp_two_day = NecessaryExpenses.objects.filter(user=request.user, time_create__month=twodaybefore.month).aggregate(Sum("sum"))
    if exp_two_day['sum__sum'] == None:
        exp_two_day['sum__sum'] = 0
    inc_three_day = Income.objects.filter(user=request.user, time_create__month=three_day.month).aggregate(Sum("sum"))
    if inc_three_day['sum__sum'] == None:
        inc_three_day['sum__sum'] = 0
    exp_three_day = NecessaryExpenses.objects.filter(user=request.user, time_create__month=three_day.month).aggregate(Sum("sum"))
    if exp_three_day['sum__sum'] == None:
        exp_three_day['sum__sum'] = 0
    inc_four_day = Income.objects.filter(user=request.user, time_create__month=four_day.month).aggregate(Sum("sum"))
    if inc_four_day['sum__sum'] == None:
        inc_four_day['sum__sum'] = 0
    exp_four_day = NecessaryExpenses.objects.filter(user=request.user, time_create__month=four_day.day).aggregate(Sum("sum"))
    if exp_four_day['sum__sum'] == None:
        exp_four_day['sum__sum'] = 0
    inc_five_day = Income.objects.filter(user=request.user, time_create__month=five_day.month).aggregate(Sum("sum"))
    if inc_five_day['sum__sum'] == None:
        inc_five_day['sum__sum'] = 0
    exp_five_day = NecessaryExpenses.objects.filter(user=request.user, time_create__month=five_day.month).aggregate(Sum("sum"))
    if exp_five_day['sum__sum'] == None:
        exp_five_day['sum__sum'] = 0
    inc_six_day = Income.objects.filter(user=request.user, time_create__month=six_day.month).aggregate(Sum("sum"))
    if inc_six_day['sum__sum'] == None:
        inc_six_day['sum__sum'] = 0
    exp_six_day = NecessaryExpenses.objects.filter(user=request.user, time_create__month=six_day.month).aggregate(Sum("sum"))
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
        "incomes": total_table(Income.objects.filter(user=request.user), request),
        "expenses": total_table(NecessaryExpenses.objects.filter(user=request.user), request),
        "total_expenses": total_exp,
        "total_income": total_inc,
        'total_save': total_save,
        'monthly_save_amount':monthly_save,
        'title': title,
        'simple': for_table_data(total_table(NecessaryExpenses.objects.filter(user=request.user), request)),
        'today_exp': exp_today,
        'today_inc': inc_today,
        'yestorday_exp': exp_yesterday,
        'yestorday_inc': inc_yesterday,
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
        NecessaryExpenses.objects.create(user=request.user, sum=dailyexp_form.cleaned_data['sum'],
                                     category=dailyexp_form.cleaned_data['category'],
                                         description = dailyexp_form.cleaned_data['description'])
        user_fin_state = FinancialStatement.objects.filter(user=request.user)
        monthly_expenses=FinancialStatement.objects.get(user=request.user)
        user_fin_state.update(expenses_live=monthly_expenses.expenses_live-dailyexp_form.cleaned_data['sum'])
        return HttpResponseRedirect(reverse('main'))
    else:
        dailyexp_form = DailyExpForm(user=user)

    dailyinc_form = DailyIncForm(request.GET, user=user)
    if request.method == "GET" and dailyinc_form.is_valid():
        Income.objects.create(user=request.user, sum=dailyinc_form.cleaned_data['sum'],
                                     category=dailyinc_form.cleaned_data['category'],
                              description = dailyinc_form.cleaned_data['description'])
        return HttpResponseRedirect(reverse('main'))
    else:
        dailyinc_form = DailyIncForm(user=user)

    total_inc=Income.objects.filter(user=request.user, time_create__day=today.day).aggregate(Sum('sum'))
    total_exp=NecessaryExpenses.objects.filter(user=request.user, time_create__day=today.day).aggregate(Sum('sum'))

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

    max_monthly_exp = monthly_save.expenses_live#monthly_save.monthly_incoms-monthly_save.monthly_target
    max_daily_exp = round(max_monthly_exp/((monthrange(2024, datetime.now().month)[1]-datetime.now().day)+1))
    different_maxexp_daylyexp= max_daily_exp-total_exp['sum__sum']
    try:
        degre_save = round(total_exp['sum__sum']/max_monthly_exp*100)
    except:
        degre_save = 0
    try:
        degre_exp=round(total_exp['sum__sum']/ round(max_monthly_exp/monthrange(2024, datetime.now().month)[1])*100)
    except ZeroDivisionError:
        degre_exp=0
    q1=NecessaryExpenses.objects.filter(user=user, time_create__day=today.day)
    q2=Income.objects.filter(user=user, time_create__day=today.day)

    content = {'title': title,
               'dailyexp': dailyexp_form,
               'dailyinc': dailyinc_form,
               'today': today,
               'table_daily_exp': total_table(NecessaryExpenses.objects.filter(time_create__day=today.day, user=request.user), request),
               'table_daily_inc':total_table(Income.objects.filter(time_create__day=today.day, user=request.user), request),
               'total_inc': total_inc,
               'total_exp': total_exp,
               'daily_save': daily_save,
               'daily_save_amount': round(daily_save_amount),
               'weekly_save_amount': round(daily_save_amount)*7,
               'monthly_save_amount': monthly_save,
               'year_save_amount': round(daily_save_amount)*365,
               'max_daily_exp': max_daily_exp,
               'degre_exp': degre_exp,
               'degre_save': degre_save,
               'daily_exp_amount': different_maxexp_daylyexp,
               'data_table': q1.union(q2).order_by('-time_create')
               }
    return render(request, 'main/index.html', content)


def total_table(model, request):
    table_category_summ = {}
    cat=[]
    for k in Category.objects.filter(user=request.user):
        cat.append(k.name)
    for c in CategoryIncomes.objects.filter(user=request.user):
        cat.append(c.name)
    for i in cat:
        res = model.filter(category__name=i).first()
        res_sum = model.filter(category__name=i).aggregate(Sum("sum"))
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
            CategoryIncomes.objects.create(user=request.user, name=add_incomes_category_form.cleaned_data['name'].upper(),
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
            Category.objects.create(user=request.user, name=add_expenses_category_form.cleaned_data['name'].upper(),
                                                description=add_expenses_category_form.cleaned_data['description'])
            return HttpResponseRedirect(reverse('addexpcat'))
    else:
        add_expenses_category_form = AddExpCategoryForm()

    content = {'title': title, 'add_expenses_category_form': add_expenses_category_form}
    return render(request, 'main/add_exp_cat.html', content)

class UserCategory(ListView):
    model = Category
    template_name = 'main/category_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        context['objects'] = Category.objects.filter(user=self.request.user)
        context['incomes'] = CategoryIncomes.objects.filter(user=self.request.user)

        return context


def user_category_delete(request, pk):
    item = get_object_or_404(Category, pk=pk)
    item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def user_income_category_delete(request, pk):
    item = get_object_or_404(CategoryIncomes, pk=pk)
    item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
        form.instance.user = self.request.user
        form.instance.expenses_live=form.instance.monthly_expenses
        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Финансовая ведомость'
        return context

def copy_col_statement(request):
    user_fin=FinancialStatement.objects.filter(user=request.id)
    copy_date = user_fin.monthly_expenses
    user_fin.update(expenses_live=copy_date)
    return user_fin

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

def daily_saved_money(request):
    monthly_save = FinancialStatement.objects.get(user=request.user)
    max_monthly_exp = monthly_save.monthly_incoms - monthly_save.monthly_target
    max_daily_exp = round(max_monthly_exp / monthrange(2024, datetime.now().month)[1])
    total_exp = NecessaryExpenses.objects.filter(user=request.user, time_create__day=today.day).aggregate(Sum('sum'))
    different_maxexp_daylyexp= max_daily_exp-total_exp['sum__sum']


def examples(request):
    return render(request, 'main/index1.html')