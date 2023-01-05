from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from accounts.models import Account, Account_Statistics

admin.site.register(Account)
admin.site.register(Account_Statistics)