from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from accounts.models import Account
from django.contrib.auth.models import User



class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'patronymic', 'location', 'school_number', 'email', 'password1',
                  'password2', 'is_teacher', 'gender')
        # fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'label': 'Фамилия'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'label': 'Имя'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-input', 'label': 'Отчество'}),

            'location': forms.Select(attrs={'class': 'form-input', 'label': 'Место учебы'}),
            'school_number': forms.NumberInput(attrs={'class': 'form-input', 'label': 'Номер школы'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'input-password'}),
            'password2': forms.PasswordInput(attrs={'class': 'input-password'}),
            'is_teacher': forms.CheckboxInput(attrs={'class': 'input-role'}),
            # 'gender': forms.RadioSelect(attrs={'class': 'input-gender'}),
            'gender': forms.Select(attrs={'class': 'form-input', 'label': 'Пол'}),
        }