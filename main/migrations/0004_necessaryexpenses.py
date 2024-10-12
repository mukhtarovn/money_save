# Generated by Django 4.2.16 on 2024-10-02 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='NecessaryExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.PositiveIntegerField(blank=True, default=0, verbose_name='СУММА')),
                ('description', models.TextField(blank=True, null=True, verbose_name='ОПИСАНИЕ')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='ДАТА СОЗДАНИЯ')),
                ('time_upate', models.DateTimeField(auto_now=True, verbose_name='ДАТА ОБНОВЛЕНИЯ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='КАТЕГОРИЯ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
