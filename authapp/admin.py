from django.contrib import admin
from authapp.models import NewUser


@admin.register(NewUser)
class PostAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email', 'age']
    ordering = ('username',)