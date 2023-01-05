from .models import Test, Question, Choice, Answer
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, DateInput, DateField, Textarea, NumberInput, TimeInput, \
    TimeField, FileInput, modelformset_factory


class DateInput(DateInput):
    input_type = 'date'


class TimeInput(TimeInput):
    input_type = 'time'


class AnswerForm(forms.Form):

    CHOICES = (
        ("1", "one"),
        ("2", "two"),
        ("3", "free"),
        ("4", "four"))
    response = forms.ChoiceField(widget=forms.RadioSelect,
              label="question.question", choices=CHOICES)


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'subject', 'text', 'difficulty', 'time', 'time_deadline', 'date_deadline', 'five',
                  'four', 'three',
                  'two']
        widgets = {
            'title': Textarea(attrs={
                'placeholder': "Проверочная работа №3",
                'class': "name-test",
                'rows':2, 'cols':50,
            }),
            'subject': Textarea(attrs={
                'placeholder': "Математика",
                'class': "name-test",
                'rows':1, 'cols':50,
            }),
            'text': Textarea(attrs={
                'class': "name-test",
                'rows':3, 'cols':50,
            }),
            'difficulty': NumberInput(attrs={
                'placeholder': "3",
                'style': 'width:50px',
                'min': '1',
                'max': '10',
                # 'class': "test-difficulty",
            }),
            'time': TimeInput(attrs={
                'placeholder': "00:15:00",
                'value':'00:15',
            }),
            'time_deadline': TimeInput(attrs={
                'placeholder': "19.12.2022"
            }),
            'date_deadline': DateInput(attrs={
                'placeholder': "19.12.2022"
            }),
            'five': NumberInput(attrs={
                'style': 'width:50px',
            }),
            'four': NumberInput(attrs={
                'style': 'width:50px',
            }),
            'three': NumberInput(attrs={
                'style': 'width:50px',
            }),
            'two': NumberInput(attrs={
                'style': 'width:50px',
            }),
        }


class QuestionsForm(ModelForm):
    class Meta:
        model = Question
        fields = ['test', 'question', 'first_answer', 'second_answer', 'third_answer', 'four_answer', 'reward',
                  'number_correct_answer']
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
                'style': 'width:50px',
            }),
            'reward': NumberInput(attrs={
                'style': 'width:50px',
            }),
        }
