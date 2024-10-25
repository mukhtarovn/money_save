# Generated by Django 4.2.16 on 2024-10-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_dailyincoms_category_remove_dailyincoms_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='income',
            options={'verbose_name': 'Доход', 'verbose_name_plural': 'Доходы'},
        ),
        migrations.AlterModelOptions(
            name='necessaryexpenses',
            options={'verbose_name': 'Расход', 'verbose_name_plural': 'Расходы'},
        ),
        migrations.AddField(
            model_name='financialstatement',
            name='expenses_live',
            field=models.PositiveIntegerField(default=0, verbose_name='Расход текущий'),
        ),
    ]
