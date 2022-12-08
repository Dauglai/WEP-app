from django.shortcuts import render
from .models import Test, Question
from .forms import TestForm, QuestionsForm

def index(request):
    return render(request, 'main/index.html')

def teacher_office(request):
    return render(request, 'teacher/teacher.html')

def constructor(request):
    test_form = TestForm()
    questions_form = QuestionsForm()
    data = {'test_form': test_form, 'questions_form': questions_form}
    return render(request, 'teacher/constructor.html', data)

def task(request):
    test = Test.objects.filter(title= "Тестовый тест")
    questions = Question.objects.filter(test__title="Тестовый тест")
    return render(request, 'teacher/task1.html', {'test': test, 'questions': questions})


