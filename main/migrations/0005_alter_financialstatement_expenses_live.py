# Generated by Django 4.2.16 on 2024-10-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_income_options_alter_necessaryexpenses_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialstatement',
            name='expenses_live',
            field=models.PositiveIntegerField(default=models.PositiveIntegerField(default=0, verbose_name='Meсячный расход'), verbose_name='Расход текущий'),
        ),
    ]
