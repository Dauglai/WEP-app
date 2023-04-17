import random

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import RegisterUserForm
from accounts.models import Account
from student.models import Account_Statistics, Protagonist, Inventory


# Create your views here.

def registration(request):
    error = ''
    if request.method == "POST":
        account_form = RegisterUserForm(request.POST)
        if account_form.is_valid():
            account_form = account_form.save(commit=False)
            account_form.save()
            Account_Statistics.objects.create(account=Account.objects.get(email=account_form.email))
            if not account_form.is_teacher:
                Protagonist.objects.create(account=Account.objects.get(email=account_form.email),
                                           name=f'Hero_{random.randrange(1, 1000, 1)}')
                Inventory.objects.create(account=Account.objects.get(email=account_form.email))
            return redirect('login')
        else:
            error = 'Форма была неверной'

    account_form = RegisterUserForm()
    data = {
        'form': account_form,
        'error': error
    }
    return render(request, 'accounts/registration.html', data)
