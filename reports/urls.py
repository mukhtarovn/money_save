from django.urls import path
import reports.views as reports

app_name = 'reports'

urlpatterns = [
    path('month/', reports.month, name='month'),
    path('last_month/', reports.last_month, name='last_month'),
]