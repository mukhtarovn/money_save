from django import forms

from .models import Category, CategoryIncomes, UserCategoryIncomes, UserCategoryExpenses, FinancialStatement


class DailyIncForm (forms.Form):
    sum = forms.IntegerField(label="СУММА")
    category = forms.ModelChoiceField(queryset=CategoryIncomes.objects.all(), label="КАТЕГОРИЯ", empty_label='Категория не выбранна')
    description = forms.CharField(max_length=100, label="ОПИСАНИЕ", required=False, widget=(forms.Textarea(attrs={'rows': 2, 'cols': 37})))


class DailyExpForm (forms.Form):
    sum = forms.IntegerField(label="СУММА")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="КАТЕГОРИЯ", empty_label='Категория не выбранна')
    description = forms.CharField(max_length=100, label="ОПИСАНИЕ", required=False, widget=(forms.Textarea(attrs={'rows': 2, 'cols': 37})))

class AddIncCategoryForm(forms.ModelForm):

    class Meta:
        model = UserCategoryIncomes
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

class AddExpCategoryForm(forms.ModelForm):

    class Meta:
        model = UserCategoryExpenses
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
