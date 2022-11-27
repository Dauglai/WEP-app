from django.shortcuts import render


def index(request):
    return render(request, 'frontMain/index.html')


def teacher_office(request):
    return render(request, 'frontMain/teacher.html')


def student_office(request):
    return render(request, 'frontMain/student.html')


def constructor(request):
    return render(request, 'frontMain/constructor.html')