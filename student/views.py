from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from student.models import AccountStatistics, Protagonist, Choice, TestRecord, Hero
from student.serializers import HeroSerializer, ProtagonistSerializer, StatisticsSerializer, TestRecordSerializer, ChoiceSerializer
from teacher.models import Test, Group
from teacher.serializers import GroupSerializer, TestSerializer


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


