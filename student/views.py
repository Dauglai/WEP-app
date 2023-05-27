from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from student.forms import JoinGroupForm
from student.models import Account_Statistics, Protagonist, Choice, Test_Record
from teacher.models import Test, Question, Group
from teacher.serializers import GroupSerializer, TestSerializer


class GropViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def list(self, request):
        user_stat = Account_Statistics.objects.get(account=request.user)
        groups = user_stat.groups.all()
        print('user:', request.user)

        groups_serializer = self.serializer_class(groups, many=True)
        return Response(groups_serializer.data, status=status.HTTP_200_OK)


class GetTestByGrop(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def list(self, request):
        user_stat = Account_Statistics.objects.get(account=request.user)
        print(user_stat)
        groups = user_stat.groups.all()
        print(groups)
        tests = get_all_tests(groups)
        tests_serializer = self.serializer_class(tests, many=True)
        return Response(tests_serializer.data)


def get_all_tests(groups):
    tasks = []
    for group in groups:
        x = Test.objects.filter(group=group)
        if x is not None:
            tasks = tasks + list(x)
    print(tasks)
    return set(tasks)


@api_view(['GET'])
def DeleteGroup(request, id):
    group = Group.objects.get(id=id)
    user_stat = Account_Statistics.objects.get(account=request.user)
    user_stat.groups.remove(group)
    return Response({'Группа исключена'})


@api_view(['POST'])
def JoinGroup(request):
    if request.method == 'POST':
        user_stat = Account_Statistics.objects.get(account=request.user)
        print(user_stat)
        login = request.data['login']
        password = request.data['password']
        print(login, password)
        con_group = Group.objects.filter(login=login) & Group.objects.filter(password=password)
        print(con_group)
        if len(con_group) > 0:
            user_stat.groups.add(con_group[0])
        return Response({'Группа подключена'})


@login_required
def student(request):
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


def task(request, task_id):
    user_stat = Account_Statistics.objects.get(account=request.user)
    task = Test.objects.get(pk=task_id)
    questions = Question.objects.filter(test__title=task.title)
    record = Test_Record.objects.create(user=request.user, test=task, count_correct=0, count_points=0)
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
        choice = Choice.objects.create(question=cur_question, number_answer=user_answer, points=cur_question.reward)
        if number_user_answer == cur_question.number_correct_answer:
            record.count_correct += 1
            record.count_points += choice.points
            user_stat.experience = user_stat.experience + 1
            user_stat.save(update_fields=["experience"])
            print('+')
        else:
            print('-')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'student/task.html', context=data)

