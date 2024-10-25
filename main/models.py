from django.conf import settings
from django.db import models

from authapp.models import NewUser

class Category(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(verbose_name='Название', max_length=64)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    time_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Пользовательская категория расхода'
        verbose_name_plural = 'Пользовательские категории расходов'

    def __str__(self):
        return self.name


class CategoryIncomes(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(verbose_name='Название', max_length=64)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    time_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Пользовательская категория доходов'
        verbose_name_plural = 'Пользовательские категории доходов'

    def __str__(self):
        return self.name

class Income(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryIncomes, on_delete=models.CASCADE, verbose_name='КАТЕГОРИЯ', default=1)
    sum = models.PositiveIntegerField(verbose_name='СУММА', default=0, blank=True)
    description = models.TextField(verbose_name='ОПИСАНИЕ', blank=True, null=True)
    time_create = models.DateTimeField(verbose_name='ДАТА СОЗДАНИЯ', auto_now_add=True, null=True)
    time_upate = models.DateTimeField(verbose_name='ДАТА ОБНОВЛЕНИЯ', auto_now=True, null=True)
    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'

    def __str__(self):
        return f"{self.user}"


class NecessaryExpenses(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='КАТЕГОРИЯ')
    sum = models.PositiveIntegerField(verbose_name='СУММА', default=0, blank=True)
    description = models.TextField(verbose_name='ОПИСАНИЕ', blank=True)
    time_create = models.DateTimeField(verbose_name='ДАТА СОЗДАНИЯ', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='ДАТА ОБНОВЛЕНИЯ', auto_now=True)
    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'
    def __str__(self):
        return F'{self.user}'

# class DailyExpenses(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='КАТЕГОРИЯ', default=1)
#     sum = models.PositiveIntegerField(verbose_name='СУММА', default=0, blank=True)
#     description = models.TextField(verbose_name='ОПИСАНИЕ', blank=True)
#     time_create = models.DateTimeField(verbose_name='ДАТА ОПЕРАЦИИ', auto_now_add=True)
#
#     class Meta:
#         verbose_name = 'Расход за день'
#         verbose_name_plural = 'Расходы за день'
#
#     def __str__(self):
#         return f'{self.user}'

# class DailyIncoms(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     category = models.ForeignKey(CategoryIncomes, on_delete=models.CASCADE, verbose_name='КАТЕГОРИЯ', default=1)
#     sum = models.PositiveIntegerField(verbose_name='СУММА', default=0, blank=True)
#     description = models.TextField(verbose_name='ОПИСАНИЕ', blank=True, null=True)
#     time_create = models.DateTimeField(verbose_name='ДАТА ОПЕРАЦИИ', auto_now_add=True)
#
#     class Meta:
#         verbose_name = 'Доход за день'
#         verbose_name_plural = 'Доходы за день'
#
#     def __str__(self):
#         return f'{self.user}'


class FinancialStatement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', unique=True)
    monthly_incoms = models.PositiveIntegerField(verbose_name='Meсячный доход', default=0)
    monthly_expenses = models.PositiveIntegerField(verbose_name='Meсячный расход', default=0)
    monthly_target = models.PositiveIntegerField(verbose_name='Цель экономии', default=0)
    expenses_live = models.PositiveIntegerField(verbose_name='Расход текущий', default=0)

    class Meta:
        verbose_name = 'Финасы'
        verbose_name_plural = 'Финасы'

    def __str__(self):
        return f'{self.user}'