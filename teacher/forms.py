from .models import Test, Question
from django.forms import ModelForm, TextInput, DateTimeInput, DateInput, DateField, Textarea, NumberInput, TimeInput, \
    TimeField, FileInput, modelformset_factory


class DateInput(DateInput):
    input_type = 'date'


class TimeInput(TimeInput):
    input_type = 'time'

"""
QuestionFormSet = modelformset_factory(
    Question, fields=('test', 'question', 'first_answer', 'second_answer', 'third_answer', 'four_answer',
                      'number_correct_answer'), extra=1)
"""
class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'difficulty', 'time', 'time_deadline', 'date_deadline', 'five', 'four', 'three',
                  'two']
        widgets = {
            'title': TextInput(attrs={
                # 'placeholder': "Название теста",
                'placeholder': "Тест №5 по Математике",
                'class': "name-test",
            }),
            'difficulty': NumberInput(attrs={
                'placeholder': "3",
                'min': '1',
                'max': '10',
                'class': "test-difficulty",
            }),
            'time': TimeInput(attrs={
                'placeholder': "00:15:00"
            }),
            'time_deadline': TimeInput(attrs={
                'placeholder': "19.12.2022"
            }),
            'date_deadline': DateInput(attrs={
                'placeholder': "19.12.2022"
            }),
        }


class QuestionsForm(ModelForm):
    class Meta:
        model = Question
        fields = ['test', 'question', 'first_answer', 'second_answer', 'third_answer', 'four_answer',
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
            }),
        }
