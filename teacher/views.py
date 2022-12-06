from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def teacher_office(request):
    return render(request, 'teacher/teacher.html')

def constructor(request):
    return render(request, 'teacher/constructor.html')

def task(request):
    return render(request, 'teacher/task1.html')
