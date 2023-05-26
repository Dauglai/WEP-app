from django.contrib import admin
from .models import Account_Statistics, Protagonist, Choice, Test_Record


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'number_answer',
        'lock_other',
    )
    list_filter = ('question',)


# Register your models here.
admin.site.register(Account_Statistics)
admin.site.register(Protagonist)
admin.site.register(Test_Record)
admin.site.register(Choice, ChoiceAdmin)
