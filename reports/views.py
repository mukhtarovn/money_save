import datetime
from django.db.models import Sum
from django.shortcuts import render

from authapp.models import NewUser
from main.models import FinancialStatement, Income, NecessaryExpenses
from main.views import total_table, for_table_data

today = datetime.datetime.now().date()

def month(request):
    title = "Отчет за месяц"
    monthly_save = FinancialStatement.objects.get(user=request.user)
    income = Income.objects.filter(user=request.user)
    expenses = NecessaryExpenses.objects.filter(user=request.user)
    total_inc = Income.objects.filter(user=request.user).aggregate(Sum('sum'))
    total_exp = NecessaryExpenses.objects.filter(user=request.user).aggregate(Sum('sum'))
    try:
        total_save = total_inc['sum__sum'] - total_exp['sum__sum']
    except:
        total_save = 0

    last = today - datetime.timedelta(days=31)
    two = today - datetime.timedelta(days=61)
    three = today - datetime.timedelta(days=91)
    four = today - datetime.timedelta(days=122)
    five = today - datetime.timedelta(days=152)
    six = today - datetime.timedelta(days=182)
    months = {'Месяц': 0, 'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6,
              'Июль': 7, 'Август': 8, 'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12}

    if request.POST:
        if request.POST['start']:
            end = today
            if request.POST['end']:
                end=request.POST['end']
            expenses = expenses.filter(time_create__gte=request.POST['start'], time_create__lte=end, user=request.user)
            income = income.filter(time_create__gte=request.POST['start'], time_create__lte=end, user=request.user)
            total_inc = Income.objects.filter(user=request.user, time_create__gte=request.POST['start'], time_create__lte=end).aggregate(Sum('sum'))
            total_exp = NecessaryExpenses.objects.filter(user=request.user, time_create__gte=request.POST['start'], time_create__lte=end).aggregate(
                Sum('sum'))

        if request.POST['month'] and request.POST['month'] != 'Месяц':
            expenses = expenses.filter(time_create__month=months[request.POST['month']], user=request.user)
            income = income.filter(time_create__month=months[request.POST['month']], user=request.user)
            total_inc = Income.objects.filter(user=request.user, time_create__month=months[request.POST['month']]).aggregate(Sum('sum'))
            total_exp = NecessaryExpenses.objects.filter(user=request.user, time_create__month=months[request.POST['month']]).aggregate(
                Sum('sum'))
        try:
            total_save = total_inc['sum__sum'] - total_exp['sum__sum']
        except:
            total_save = 0

    inc_today = Income.objects.filter(user=request.user, time_create__month=today.month).aggregate(Sum("sum"))
    if inc_today['sum__sum'] == None:
        inc_today['sum__sum'] = 0
    exp_today = NecessaryExpenses.objects.filter(user=request.user, time_create__month=today.month).aggregate(Sum("sum"))
    if exp_today['sum__sum'] == None:
        exp_today['sum__sum'] = 0
    inc_yesterday = Income.objects.filter(user=request.user, time_create__month=last.month).aggregate(Sum("sum"))
    if inc_yesterday['sum__sum'] == None:
        inc_yesterday['sum__sum'] = 0
    exp_yesterday = NecessaryExpenses.objects.filter(user=request.user, time_create__day=last.day).aggregate(
        Sum("sum"))
    if exp_yesterday['sum__sum'] == None:
        exp_yesterday['sum__sum'] = 0
    inc_two_day = Income.objects.filter(user=request.user, time_create__day=two.day).aggregate(Sum("sum"))
    if inc_two_day['sum__sum'] == None:
        inc_two_day['sum__sum'] = 0
    exp_two_day = NecessaryExpenses.objects.filter(user=request.user, time_create__day=two.day).aggregate(Sum("sum"))
    if exp_two_day['sum__sum'] == None:
        exp_two_day['sum__sum'] = 0
    inc_three_day = Income.objects.filter(user=request.user, time_create__day=three.day).aggregate(Sum("sum"))
    if inc_three_day['sum__sum'] == None:
        inc_three_day['sum__sum'] = 0
    exp_three_day = NecessaryExpenses.objects.filter(user=request.user, time_create__day=three.day).aggregate(Sum("sum"))
    if exp_three_day['sum__sum'] == None:
        exp_three_day['sum__sum'] = 0
    inc_four_day = Income.objects.filter(user=request.user, time_create__day=four.day).aggregate(Sum("sum"))
    if inc_four_day['sum__sum'] == None:
        inc_four_day['sum__sum'] = 0
    exp_four_day = NecessaryExpenses.objects.filter(user=request.user, time_create__day=four.day).aggregate(Sum("sum"))
    if exp_four_day['sum__sum'] == None:
        exp_four_day['sum__sum'] = 0
    inc_five_day = Income.objects.filter(user=request.user, time_create__day=five.day).aggregate(Sum("sum"))
    if inc_five_day['sum__sum'] == None:
        inc_five_day['sum__sum'] = 0
    exp_five_day = NecessaryExpenses.objects.filter(user=request.user, time_create__day=five.day).aggregate(Sum("sum"))
    if exp_five_day['sum__sum'] == None:
        exp_five_day['sum__sum'] = 0
    inc_six_day = Income.objects.filter(user=request.user, time_create__day=six.day).aggregate(Sum("sum"))
    if inc_six_day['sum__sum'] == None:
        inc_six_day['sum__sum'] = 0
    exp_six_day = NecessaryExpenses.objects.filter(user=request.user, time_create__day=six.day).aggregate(Sum("sum"))
    if exp_six_day['sum__sum'] == None:
        exp_six_day['sum__sum'] = 0
    # months={'Январь':'Jan', 'Февраль':'Feb', 'Март': 'Mar','Апрель': 'Apr','Май': 'May','Июнь':  'Jun', 'Июль': 'Jul',
    #         'Август':'Aug','Сентябрь': 'Sep', 'Октябрь':  'Oct', 'Ноябрь':'Nov', 'Декабрь': 'Dec'}

    content = {
        "users": NewUser.objects.all(),
        "today": today,
        "start_search_defolt": (today - datetime.timedelta(days=31)).strftime("%Y-%m-%d"),
        "today_for_search": today.strftime("%Y-%m-%d"),
        'months': months,
        "yestorday": last.strftime("%b"),
        "twodaybefore": two.strftime("%b"),
        "threedaybefore": three.strftime("%b"),
        "fourdaybefore": four.strftime("%b"),
        "fivedaybefore": five.strftime("%b"),
        "sixdaybefore": six.strftime("%b"),
        "incomes": total_table(income, request),
        "expenses": total_table(expenses, request),
        "total_expenses": total_exp,
        "total_income": total_inc,
        'total_save': total_save,
        'monthly_save_amount': monthly_save,
        'title': title,
        'simple': for_table_data(total_table(expenses, request)),
        'today_exp': exp_today,
        'today_inc': inc_today,
        'all_expenses': expenses,
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
    return render(request, 'reports/month.html', content)

# def last_month(request):
#     title = "Отчет за месяц"
#     month = datetime.datetime.now().month - 1
#     monthly_save = FinancialStatement.objects.get(user=request.user)
#     try:
#         total_inc = Income.objects.filter(user=request.user, time_create__month=month).aggregate(Sum('sum'))
#     except:
#         total_inc=0
#     try:
#         total_exp = NecessaryExpenses.objects.filter(user=request.user, time_create__month=month).aggregate(Sum('sum'))
#     except:
#         total_exp=0
#
#     try:
#         total_save = total_inc['sum__sum'] - total_exp['sum__sum']
#     except:
#         total_save = 0
#     last = today - datetime.timedelta(days=31)
#     two = today - datetime.timedelta(days=61)
#     three = today - datetime.timedelta(days=91)
#     four = today - datetime.timedelta(days=122)
#     five = today - datetime.timedelta(days=152)
#     six = today - datetime.timedelta(days=182)
#
#     inc_today = Income.objects.filter(user=request.user, time_create__month=month).aggregate(Sum("sum"))
#     if inc_today['sum__sum'] == None:
#         inc_today['sum__sum'] = 0
#     exp_today = NecessaryExpenses.objects.filter(user=request.user, time_create__month=month).aggregate(
#         Sum("sum"))
#     if exp_today['sum__sum'] == None:
#         exp_today['sum__sum'] = 0
#     inc_yesterday = Income.objects.filter(user=request.user, time_create__month=last.month).aggregate(Sum("sum"))
#     if inc_yesterday['sum__sum'] == None:
#         inc_yesterday['sum__sum'] = 0
#     exp_yesterday = NecessaryExpenses.objects.filter(user=request.user, time_create__month=last.month).aggregate(
#         Sum("sum"))
#     if exp_yesterday['sum__sum'] == None:
#         exp_yesterday['sum__sum'] = 0
#     inc_two_day = Income.objects.filter(user=request.user, time_create__month=two.month).aggregate(Sum("sum"))
#     if inc_two_day['sum__sum'] == None:
#         inc_two_day['sum__sum'] = 0
#     exp_two_day = NecessaryExpenses.objects.filter(user=request.user, time_create__month=two.month).aggregate(Sum("sum"))
#     if exp_two_day['sum__sum'] == None:
#         exp_two_day['sum__sum'] = 0
#     inc_three_day = Income.objects.filter(user=request.user, time_create__month=three.month).aggregate(Sum("sum"))
#     if inc_three_day['sum__sum'] == None:
#         inc_three_day['sum__sum'] = 0
#     exp_three_day = NecessaryExpenses.objects.filter(user=request.user, time_create__month=three.month).aggregate(Sum("sum"))
#     if exp_three_day['sum__sum'] == None:
#         exp_three_day['sum__sum'] = 0
#     inc_four_day = Income.objects.filter(user=request.user, time_create__month=four.month).aggregate(Sum("sum"))
#     if inc_four_day['sum__sum'] == None:
#         inc_four_day['sum__sum'] = 0
#     exp_four_day = NecessaryExpenses.objects.filter(user=request.user, time_create__month=four.month).aggregate(Sum("sum"))
#     if exp_four_day['sum__sum'] == None:
#         exp_four_day['sum__sum'] = 0
#     inc_five_day = Income.objects.filter(user=request.user, time_create__month=five.month).aggregate(Sum("sum"))
#     if inc_five_day['sum__sum'] == None:
#         inc_five_day['sum__sum'] = 0
#     exp_five_day = NecessaryExpenses.objects.filter(user=request.user, time_create__month=five.month).aggregate(Sum("sum"))
#     if exp_five_day['sum__sum'] == None:
#         exp_five_day['sum__sum'] = 0
#     inc_six_day = Income.objects.filter(user=request.user, time_create__month=six.month).aggregate(Sum("sum"))
#     if inc_six_day['sum__sum'] == None:
#         inc_six_day['sum__sum'] = 0
#     exp_six_day = NecessaryExpenses.objects.filter(user=request.user, time_create__month=six.month).aggregate(Sum("sum"))
#     if exp_six_day['sum__sum'] == None:
#         exp_six_day['sum__sum'] = 0
#
#     content = {
#         "users": NewUser.objects.all(),
#         "today": today,
#         "yestorday": last.strftime("%b"),
#         "twodaybefore": two.strftime("%b"),
#         "threedaybefore": three.strftime("%b"),
#         "fourdaybefore": four.strftime("%b"),
#         "fivedaybefore": five.strftime("%b"),
#         "sixdaybefore": six.strftime("%b"),
#         "incomes": total_table(Income.objects.filter(user=request.user, time_create__month=month), request),
#         "expenses": total_table(NecessaryExpenses.objects.filter(user=request.user, time_create__month=month), request),
#         "total_expenses": total_exp,
#         "total_income": total_inc,
#         'total_save': total_save,
#         'monthly_save_amount': monthly_save,
#         'title': title,
#         'simple': for_table_data(total_table(NecessaryExpenses.objects.filter(user=request.user, time_create__month=month), request)),
#         'today_exp': exp_today,
#         'today_inc': inc_today,
#         'yestorday_exp': exp_yesterday,
#         'yestorday_inc': inc_yesterday,
#         'twodaybefore_exp': exp_two_day,
#         'twodaybefore_inc': inc_two_day,
#         'threedaybefore_exp': exp_three_day,
#         'threedaybefore_inc': inc_three_day,
#         'fourdaybefore_exp': exp_four_day,
#         'fourdaybefore_inc': inc_four_day,
#         'fivedaybefore_exp': exp_five_day,
#         'fivedaybefore_inc': inc_five_day,
#         'sixdaybefore_exp': exp_six_day,
#         'sixdaybefore_inc': inc_six_day,
#     }
#     return render(request, 'reports/month.html', content)

