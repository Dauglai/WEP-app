from django.shortcuts import render, redirect
from .models import Test, Question
from .forms import TestForm, QuestionsForm

def index(request):
    return render(request, 'main/index.html')

def teacher_office(request):
    return render(request, 'teacher/teacher.html')

def constructor(request):
    error = ''
    if request.method == "POST":
        test_form = TestForm(request.POST)
        questions_form = QuestionsForm(request.POST)
        questions_form.test = test_form
        if test_form.is_valid():
            test_form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    test_form = TestForm()
    questions_form = QuestionsForm()
    data = {
        'test_form': test_form,
        'questions_form': questions_form,
        'error': error
    }
    return render(request, 'teacher/constructor.html', data)

def task(request):
    test = Test.objects.filter(title= "Тестовый тест")
    questions = Question.objects.filter(test__title="Тестовый тест")
    return render(request, 'teacher/task1.html', {'test': test, 'questions': questions})


