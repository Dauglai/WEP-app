from django.template.response import TemplateResponse
from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.models import Account
from student.forms import JoinGroupForm
from teacher.models import Test, Question, Group

def index(request):
    return render(request, 'main/index.html')

def rating_table(request):
    return render(request, 'main/rating_table.html')

def student(request):
    tests = request.user.test_set.all()
    groups = request.user.group_set.all()

    if request.method == "POST":
        login = request.POST.get("login")
        print(login)
        password = request.POST.get("password")
        print(password)
        con_group = Group.objects.filter(login=login) & Group.objects.filter(password=password)
        if len(con_group) > 0:
            print(con_group[0].owner)
            con_group[0].owner = Account.objects.get(pk=(request.user.id))
            groups = request.user.group_set.all()
        print(con_group)

    group_form = JoinGroupForm()
    data = {
        'group_form': group_form,
        'tests': tests,
        'groups': groups,
    }
    return TemplateResponse(request, 'student/student.html', data)

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
