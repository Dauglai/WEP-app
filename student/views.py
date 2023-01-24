from django.db.models import QuerySet
from django.template.response import TemplateResponse
from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import render
from django.shortcuts import render, redirect

from accounts.models import Account
from student.forms import JoinGroupForm
from student.models import Account_Statistics
from teacher.models import Test, Question, Group

def getAllTests(groups):
    tasks = []
    for group in groups:
        x = group.tasks.all()
        if x is not None:
            tasks = tasks + list(x)
    #         Выборка без одинаковых
    #         Сравнивать по id
    print(tasks)
    return tasks


def index(request):
    return render(request, 'main/index.html')

def student(request):
    user_stat = Account_Statistics.objects.get(account=request.user)

    groups = user_stat.groups.all()
    tasks = getAllTests(groups)

    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        con_group = Group.objects.filter(login=login) & Group.objects.filter(password=password)
        print(con_group)
        if len(con_group) > 0:
            user_stat.groups.add(con_group[0])

            groups = user_stat.groups.all()
            tasks = getAllTests(groups)

    group_form = JoinGroupForm()
    data = {
        'group_form': group_form,
        'tasks': tasks,
        'groups': groups,
    }
    return TemplateResponse(request, 'student/student.html', data)

def task(request, task_id):
    task = Test.objects.get(pk=task_id)
    questions = Question.objects.filter(test__title=task.title)
    data = {
        'test': task,
        'questions': questions
    }
    return render(request, 'student/task.html', context=data)
