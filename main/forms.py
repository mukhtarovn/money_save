from urllib import request

from django import forms
import requests

from .models import Category, CategoryIncomes, FinancialStatement, Income, NecessaryExpenses


class DailyIncForm (forms.ModelForm):
    # model = Income
    # sum = forms.IntegerField(label="СУММА")
    # category = forms.ModelChoiceField(queryset=CategoryIncomes.objects.all(), label="КАТЕГОРИЯ", empty_label='Категория не выбранна')
    # description = forms.CharField(max_length=100, label="ОПИСАНИЕ", required=False, widget=(forms.Textarea(attrs={'rows': 2, 'cols': 37})))
    class Meta:
        model = Income
        fields = ['sum', 'category', 'description']
        categoryes = forms.ModelChoiceField(queryset=None)
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 37})
        }

    def __init__(self, *args, **kwargs):
        # get 'user' param from kwargs
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = CategoryIncomes.objects.filter(user=self.user)
        self.fields['category'].empty_label = 'Категория не выбрана'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class DailyExpForm (forms.ModelForm):
    class Meta:
        model = NecessaryExpenses
        fields = ['sum', 'category', 'description']
        categoryes= forms.ModelChoiceField(queryset=None)
        widgets={
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 37})
        }
    def __init__(self, *args, **kwargs):
        # get 'user' param from kwargs
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=self.user)
        self.fields['category'].empty_label = 'Категория не выбрана'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

class AddIncCategoryForm(forms.ModelForm):

    class Meta:
        model = CategoryIncomes
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

class AddExpCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

class FinancialStatementForm(forms.ModelForm):

    class Meta:
        model = FinancialStatement
        fields = ['monthly_incoms', 'monthly_expenses', 'monthly_target']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

