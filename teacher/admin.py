from django.contrib import admin
from .models import Test, Question
from django.contrib import admin
from .models import Question, Answer, Choice, Group


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


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'question',
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


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Test)
admin.site.register(Group)
# Register your models here.
