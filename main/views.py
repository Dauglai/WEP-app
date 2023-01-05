from django.shortcuts import render
from django.views.generic import ListView

from accounts.models import Account_Statistics
from teacher.models import Test


def index(request):
    return render(request, 'main/index.html')

def teacher_office(request):
    return render(request, 'teacher/teacher.html')

def constructor(request):
    return render(request, 'teacher/constructor.html')

# def student_office(request):
#     return render(request, 'student/student.html')

class TestListView(ListView):
    model = Test
    template_name = "student/student.html"

class StatisticListView(ListView):
    model = Account_Statistics
    template_name = "main/rating_table.html"

# def second_page(request):
#     if request.user.is_teacher or request.user.admin:
#         return render(request, 'teacher/teacher.html')
#     else:
#         return render(request, 'student/student.html')

def login(request):
    return render(request, 'registration/login.html')

