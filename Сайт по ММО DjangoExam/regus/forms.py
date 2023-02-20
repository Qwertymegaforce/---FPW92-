from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(forms.ModelForm):
    temp_user_username = forms.CharField(label='Логин', widget=forms.TextInput)
    temp_user_email = forms.EmailField(label='Адрес электронной почты', widget=forms.EmailInput())
    temp_user_password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    temp_user_password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = ModelTempUser
        fields = ('temp_user_username', 'temp_user_email', 'temp_user_password1', 'temp_user_password2')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('temp_user_password1')
        password2 = cleaned_data.get('temp_user_password2')

        if password1 != password2:
            raise ValidationError('Пароли не совпадают')

        elif len(password1) < 8:
            raise ValidationError('Пароль не менее 8 символов!')

        elif password1.isalpha() or password1.isdigit():
            raise ValidationError('Ваш пароль состоит только из чисел/букв, и потому слишком простой!')

        elif password1.islower():
            raise ValidationError('Добавьте в пароль символы верхнего регистра!')

        elif password1.isupper():
            raise ValidationError('Добавьте в пароль символы нижнего регистра!')

        return cleaned_data
