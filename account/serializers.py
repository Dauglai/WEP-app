from django.contrib.auth.models import User
from rest_framework import serializers
from .models import AccountManager, Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'last_name', 'first_name', 'patronymic', 'location', 'school_number',
                  'email', 'is_teacher', 'gender', 'is_staff', 'is_admin', 'is_superuser')