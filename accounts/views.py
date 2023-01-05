from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import RegisterUserForm


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = RegisterUserForm #UserCreationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('login')
    # template_name = 'registration.html'

# def registration(request):
#     return render(request, 'accounts/signup.html')