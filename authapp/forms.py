from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import forms

from .models import NewUser

class NewUserLoginForm(AuthenticationForm):
    class Meta:
        model = NewUser
        fields = ('name', 'password')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

class NewUserRegisterForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age')
        labels = {'username': 'Ник', 'first_name': 'Имя', 'email': 'Адрес эл. почта',
                  'password1': "Пароль", 'password2': "Подтверджение" }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            self.fields['username'].widget.attrs['lable'] = 'Имя'

class NewUserEditForm(UserChangeForm):
    class Meta:
        model = NewUser
        fields = ('username', 'first_name', 'email', 'age')
        labels = {'username': 'Ник', 'first_name': 'Имя', 'email': 'Адрес эл. почта'}
    def __init__(self, *args, **kwargs):
        super(NewUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text=''
            # if field_name == 'password':
            #      field.widget = forms.as_hidden


