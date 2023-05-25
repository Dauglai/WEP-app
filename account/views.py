import random

from django.db.models.signals import post_save
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.forms import RegisterUserForm
from account.models import Account
from account.serializers import AccountSerializer
from student.models import Account_Statistics, Protagonist, Inventory
from student.serializers import StatisticsSerializer


class RegistrUserView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class CreateStatistics(CreateAPIView):
    queryset = Account_Statistics.objects.all()
    serializer_class = StatisticsSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = StatisticsSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class UserByToken(APIView):
    def post(self, request):
        data = {
            'id': str(request.user.id),
            'email': str(request.user.email),
            'last_name': str(request.user.last_name),
            'first_name': str(request.user.first_name),
            'patronymic': str(request.user.patronymic),

            'location': str(request.user.location),
            'school_number': str(request.user.school_number),
            'is_teacher': str(request.user.is_teacher),
            'gender': str(request.user.gender),
        }
        print(data.values())
        return Response(data, status=status.HTTP_201_CREATED)



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

