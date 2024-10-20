# Generated by Django 4.2.16 on 2024-10-18 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользовательская категория расхода',
                'verbose_name_plural': 'Пользовательские категории расходов',
            },
        ),
        migrations.CreateModel(
            name='CategoryIncomes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользовательская категория доходов',
                'verbose_name_plural': 'Пользовательские категории доходов',
            },
        ),
        migrations.CreateModel(
            name='NecessaryExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.PositiveIntegerField(blank=True, default=0, verbose_name='СУММА')),
                ('description', models.TextField(blank=True, verbose_name='ОПИСАНИЕ')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='ДАТА СОЗДАНИЯ')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='ДАТА ОБНОВЛЕНИЯ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='КАТЕГОРИЯ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Расход за месяц',
                'verbose_name_plural': 'Расходы за месяц',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.PositiveIntegerField(blank=True, default=0, verbose_name='СУММА')),
                ('description', models.TextField(blank=True, null=True, verbose_name='ОПИСАНИЕ')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='ДАТА СОЗДАНИЯ')),
                ('time_upate', models.DateTimeField(auto_now=True, null=True, verbose_name='ДАТА ОБНОВЛЕНИЯ')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.categoryincomes', verbose_name='КАТЕГОРИЯ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Доход за месяц',
                'verbose_name_plural': 'Доходы за месяц',
            },
        ),
        migrations.CreateModel(
            name='FinancialStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_incoms', models.PositiveIntegerField(default=0, verbose_name='Meсячный доход')),
                ('monthly_expenses', models.PositiveIntegerField(default=0, verbose_name='Meсячный расход')),
                ('monthly_target', models.PositiveIntegerField(default=0, verbose_name='Цель экономии')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Финасы',
                'verbose_name_plural': 'Финасы',
            },
        ),
        migrations.CreateModel(
            name='DailyIncoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.PositiveIntegerField(blank=True, default=0, verbose_name='СУММА')),
                ('description', models.TextField(blank=True, null=True, verbose_name='ОПИСАНИЕ')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='ДАТА ОПЕРАЦИИ')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.categoryincomes', verbose_name='КАТЕГОРИЯ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Доход за день',
                'verbose_name_plural': 'Доходы за день',
            },
        ),
        migrations.CreateModel(
            name='DailyExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.PositiveIntegerField(blank=True, default=0, verbose_name='СУММА')),
                ('description', models.TextField(blank=True, verbose_name='ОПИСАНИЕ')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='ДАТА ОПЕРАЦИИ')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='КАТЕГОРИЯ')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Расход за день',
                'verbose_name_plural': 'Расходы за день',
            },
        ),
    ]
