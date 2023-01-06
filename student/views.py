from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from teacher.models import Test, Question

def index(request):
    return render(request, 'main/index.html')

def rating_table(request):
    return render(request, 'main/rating_table.html')

class TestListView(ListView):
    model = Test
    template_name = "student.html"

def task(request):
    test = Test.objects.get(pk=(Test.objects.last()).id)
    questions = Question.objects.filter(test__title=test.title)
    data = {
        'test': test,
        'questions': questions
    }
    return render(request, 'student/task1.html', data)
