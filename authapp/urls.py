from django.urls import path
import authapp.views as authap

app_name = 'authapp'

urlpatterns = [
    path('login/', authap.login, name='login'),
    path('logout/', authap.logout, name='logout'),
    path('register/', authap.register, name='register'),
    path('edit/', authap.edit, name='edit'),
]