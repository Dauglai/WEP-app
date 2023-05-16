from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from student.forms import JoinGroupForm
from student.models import Account_Statistics, Protagonist, Choice, Test_Record
from teacher.models import Test, Question, Group


def getAllTests(groups):
    tasks = []
    for group in groups:
        x = group.tasks.all()
        if x is not None:
            tasks = tasks + list(x)
    print(tasks)
    return tasks


@login_required
def student(request):
    request.session['flag'] = True
    if request.user.is_teacher and request.user.is_staff and request.user.is_admin:
        return redirect('main')
    user_stat = Account_Statistics.objects.get(account=request.user)
    user_protagonist = Protagonist.objects.get(account=request.user)
    groups = user_stat.groups.all()
    tasks = Test.objects.all()

    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        con_group = Group.objects.filter(login=login) & Group.objects.filter(password=password)
        print(con_group)
        if len(con_group) > 0:
            user_stat.groups.add(con_group[0])
            groups = user_stat.groups.all()
            tasks = Test.objects.all()

    group_form = JoinGroupForm()
    data = {
        'group_form': group_form,
        'tasks': tasks,
        'groups': groups,
        'balance': user_stat.balance,
        'protagonist': user_protagonist,
    }
    print(f'Hero_{request.user.id}')
    return TemplateResponse(request, 'student/student.html', data)


def protagonist(request):
    if request.user.is_teacher and request.user.is_staff and request.user.is_admin:
        return redirect('main')
    return render(request, 'student/protagonist.html')


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
        choice = Choice.objects.create(question=cur_question, number_answer=number_user_answer)
    return render(request, 'student/task.html', context=data)


def results(request, id):
    task = Test.objects.get(pk=id)
    count_correct = 0
    points = 0
    questions = Question.objects.filter(test__title=task.title)
    for cur_question in questions:
        if cur_question.choice.number_answer == cur_question.number_correct_answer:
            count_correct += 1
            points += cur_question.reward
            #user_stat.experience = user_stat.experience + 1
            #user_stat.save(update_fields=["experience"])

    record = Test_Record.objects.create(user=request.user, test=task, count_correct=count_correct, count_points=points)
    return student(request)


def watch_group(request, id):
    group = Group.objects.get(id=id)
    all_accounts = Account_Statistics.objects.all()
    participants = all_accounts.filter(groups=group)

    data = {
        'participants': participants,
    }
    return render(request, 'student/watch-group.html', context=data)


def delete_group(request, id):
    try:
        group = Group.objects.get(id=id)
        user_stat = Account_Statistics.objects.get(account=request.user)
        user_stat.groups.remove(group)
        # print(user_stat.groups)
        return redirect("student")
    except Group.DoesNotExist:
        return redirect("student")

