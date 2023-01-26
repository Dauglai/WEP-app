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
    user_stat = Account_Statistics.objects.get(account=request.user)
    task = Test.objects.get(pk=task_id)
    questions = Question.objects.filter(test__title=task.title)

    transcripts = {
        1: 'first_answer',
        2: 'second_answer',
        3: 'third_answer',
        4: 'four_answer',
    }

    data = {
        'test': task,
        'questions': questions
    }

    if request.method == "POST":
        response = request.POST
        print(response)
        cur_question = questions.get(id=response['id'])
        user_answer = response['answer']
        number_user_answer = 0
        for key in transcripts:
            if getattr(cur_question, transcripts[key]) == user_answer:
                number_user_answer = key
        if number_user_answer == cur_question.number_correct_answer:
            user_stat.experience =user_stat.experience + 1
            user_stat.save(update_fields=["experience"])
            print('+')
        else:
            print('-')

    return render(request, 'student/task.html', context=data)

