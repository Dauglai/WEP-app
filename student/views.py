from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.models import Account
from student.models import AccountStatistics, Protagonist, Choice, TestRecord, Hero
from student.serializers import HeroSerializer, ProtagonistSerializer, StatisticsSerializer, \
    TestRecordSerializer, ChoiceSerializer
from teacher.models import Test, Question, Group
from teacher.serializers import GroupSerializer, TestSerializer
from rest_framework import filters


class GropViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def list(self, request):
        user_stat = AccountStatistics.objects.get(account=request.user)
        groups = user_stat.groups.all()
        print('user:', request.user)

        groups_serializer = self.serializer_class(groups, many=True)
        return Response(groups_serializer.data, status=status.HTTP_200_OK)


class GetTestByGrop(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def list(self, request):
        user_stat = AccountStatistics.objects.get(account=request.user)
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


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def get(self, request):
        hero = Hero.objects.get(pk=self.kwargs['pk'])
        hero_serializer = self.serializer_class(hero)
        return Response(hero_serializer.data, status=status.HTTP_200_OK)


class ProtagonistViewSet(viewsets.ModelViewSet):
    queryset = Protagonist.objects.all()
    serializer_class = ProtagonistSerializer

    def list(self, request):
        protagonist = Protagonist.objects.get(account=request.user)
        protagonist_serializer = self.serializer_class(protagonist)
        return Response(protagonist_serializer.data)


class TestRecordViewSetList(viewsets.ViewSet):
    queryset = TestRecord.objects.all()
    serializer_class = TestRecordSerializer

    def list(self, request):
        test_record = TestRecord.objects.filter(user=request.user)
        test_record_serializer = self.serializer_class(test_record, many=True)
        return Response(test_record_serializer.data)


class TestRecordViewSet(viewsets.ModelViewSet):
    queryset = TestRecord.objects.all()
    serializer_class = TestRecordSerializer

    def create(self, request):
        print(request.data['test'])
        test_record = TestRecord.objects.create(
            user=request.user,
            user_name=f'{request.user.last_name} {request.user.first_name} {request.user.patronymic}',
            test=Test.objects.get(pk=request.data['test']),
            test_name=request.data['test_name'],
            count_correct=request.data['count_correct'],
            grades=request.data['grades'],
            count_points=request.data['count_points'],
        )
        test_record_serializer = self.serializer_class(test_record)
        return Response(test_record_serializer.data)

    def update(self, request, pk=None):
        pass


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class AccountStatisticsViewSet(viewsets.ModelViewSet):
    queryset = AccountStatistics.objects.all()
    serializer_class = StatisticsSerializer

    def list(self, request):
        user_stat = AccountStatistics.objects.get(account=request.user)
        # login = request.data['login']
        # password = request.data['password']
        user_stat_serializer = self.serializer_class(user_stat)
        return Response(user_stat_serializer.data)

    def update(self, request, pk=None):
        user_stat = AccountStatistics.objects.get(account=request.user)
        i = request.data['i']
        user_stat.experience += i
        print('experience', user_stat.experience)
        user_stat.save()
        user_stat_serializer = self.serializer_class(user_stat)
        return Response(user_stat_serializer.data)


class AllAccountStatisticsViewSet(viewsets.ModelViewSet):
    queryset = AccountStatistics.objects.all()
    serializer_class = StatisticsSerializer


@api_view(['GET'])
def DeleteGroup(request, id):
    group = Group.objects.get(id=id)
    user_stat = AccountStatistics.objects.get(account=request.user)
    user_stat.groups.remove(group)
    return Response({'Группа исключена'})


@api_view(['POST'])
def JoinGroup(request):
    if request.method == 'POST':
        user_stat = AccountStatistics.objects.get(account=request.user)
        print(user_stat)
        login = request.data['login']
        password = request.data['password']
        print(login, password)
        con_group = Group.objects.filter(login=login) & Group.objects.filter(password=password)
        print(con_group)
        if len(con_group) > 0:
            user_stat.groups.add(con_group[0])
        return Response({'Группа подключена'})


@api_view(['POST'])
def RewardStudent(request):
    if request.method == 'POST':
        user_stat = AccountStatistics.objects.get(account=request.user)
        print(user_stat)
        score = request.data['score']
        exp = request.data['exp']
        user_stat.experience = user_stat.experience + exp
        user_stat.score = user_stat.score + score
        user_stat.save()
        return Response({'Транзакция прошла успешно'})


@login_required
def student(request):
    if request.user.is_teacher and request.user.is_staff and request.user.is_admin:
        return redirect('main')
    user_stat = AccountStatistics.objects.get(account=request.user)
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

    data = {
        # 'group_form': group_form,
        'tasks': tasks,
        'groups': groups,
        'balance': user_stat.balance,
        'protagonist': user_protagonist,
    }
    print(f'Hero_{request.user.id}')
    return TemplateResponse(request, 'student/student.html', data)


def task(request, task_id):
    user_stat = AccountStatistics.objects.get(account=request.user)
    task = Test.objects.get(pk=task_id)
    questions = Question.objects.filter(test__title=task.title)
    record = TestRecord.objects.create(user=request.user, test=task, count_correct=0, count_points=0)
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

