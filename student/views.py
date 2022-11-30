from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def student_office(request):
    return render(request, 'student/student.html')
