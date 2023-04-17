from django.contrib import admin
from .models import Account_Statistics, Protagonist, Item, Inventory

# Register your models here.
admin.site.register(Account_Statistics)
admin.site.register(Protagonist)
admin.site.register(Item)
admin.site.register(Inventory)
