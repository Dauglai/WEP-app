from .models import Test, Question
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, NumberInput, TimeInput, FileInput


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'time', 'difficulty', 'deadline', 'boss', 'five', 'four', 'three', 'two']
        widgets = {
            'title': TextInput(attrs={
                'placeholder': "Название теста"
            }),
            'time': TimeInput(attrs={
                'placeholder': "Время выполнения"
            }),
            'deadline': DateTimeInput(attrs={
                'placeholder': "Срок сдачи"
            }),
            'boss': FileInput(attrs={
                'placeholder': "Выбрать босса"
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
        widgets = {
            'question': TextInput(attrs={
                'placeholder': "Поле для ввода вопроса",
                'class': "form-control"
            }),
            'first_answer': TextInput(attrs={
                'placeholder': "Ответ",
                'class': "answer"
            }),
            'second_answer': TextInput(attrs={
                'placeholder': "Ответ",
                'class': "answer"
            }),
            'third_answer': TextInput(attrs={
                'placeholder': "Ответ",
                'class': "answer"
            }),
            'four_answer': TextInput(attrs={
                'placeholder': "Ответ",
                'class': "answer"
            }),
            'number_correct_answer': NumberInput(attrs={
            }),
        }