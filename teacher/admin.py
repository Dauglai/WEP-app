from django.contrib import admin
from .models import Test, Question, Group, Boss
from django.contrib import admin


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'test',
        'question',
        'first_answer',
        'second_answer',
        'third_answer',
        'four_answer',
        'reward',
        'number_correct_answer'
    )


admin.site.register(Group)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Test)
admin.site.register(Boss)
# Register your models here.
