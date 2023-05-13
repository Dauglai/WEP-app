from django.contrib import admin
from .models import Account_Statistics, Protagonist, Item, Inventory, Answer, Choice


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'number_answer',
        'points',
        'lock_other',
    )
    list_filter = ('question',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'choice',
    )
    list_filter = ('user',)


# Register your models here.
admin.site.register(Account_Statistics)
admin.site.register(Protagonist)
admin.site.register(Item)
admin.site.register(Inventory)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)