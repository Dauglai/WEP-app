from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def teacher_office(request):
    return render(request, 'teacher/teacher.html')

def constructor(request):
    return render(request, 'teacher/constructor.html')

def student_office(request):
    return render(request, 'student/student.html')

def registration(request):
    return render(request, 'registration/registration.html')

def login(request):
    return render(request, 'registration/login.html')

