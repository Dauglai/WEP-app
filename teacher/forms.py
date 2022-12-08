from .models import Test, Question
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, NumberInput


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'time', 'difficulty', 'deadline', 'boss', 'five', 'four', 'three', 'two']
        widgets = {
            'title': TextInput(attrs={
                'placeholder': "Название теста"
            }),
            'time': TextInput(attrs={
                'placeholder': "Название теста"
            }),
            'deadline': DateTimeInput(attrs={
                'placeholder': "Название теста"
            }),
            'boss': TextInput(attrs={
                'placeholder': "Название теста"
            }),
            'difficulty': NumberInput(attrs={
                'placeholder': "Сложность",
                'min': '1',
                'max': '10'
            }),
        }


class QuestionsForm(ModelForm):
    class Meta:
        model = Question
        fields = ['test', 'question', 'first_answer', 'second_answer', 'third_answer', 'four_answer', 'number_correct_answer']
