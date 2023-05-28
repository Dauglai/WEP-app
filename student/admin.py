from django.contrib import admin
from .models import AccountStatistics, Protagonist, Choice, TestRecord, Hero


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'number_answer',
        'lock_other',
    )
    list_filter = ('question',)


# Register your models here.
admin.site.register(AccountStatistics)
admin.site.register(Protagonist)
admin.site.register(Hero)
admin.site.register(TestRecord)
admin.site.register(Choice, ChoiceAdmin)
