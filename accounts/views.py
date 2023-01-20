from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import RegisterUserForm
from student.models import Account_Statistics


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('login')

    # def form_valid(self, form):
    #     if not form.is_teacher:
    #         Account_Statistics.objects.create(account= form.id)
    #         # form.instance.created_by = self.request.user
    #     return super().form_valid(form)