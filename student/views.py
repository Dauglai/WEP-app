from django.views.generic import ListView, TemplateView
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

# def task(request):
#     test = Test.objects.filter()
#     questions = Question.objects.filter()
#     return render(request, 'teacher/task1.html', {'test': test, 'questions': questions})
