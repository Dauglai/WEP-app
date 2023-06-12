
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from account.models import Account
from account.serializers import AccountGetSerializer
from student.models import AccountStatistics
from .models import Test, Question, Group, Boss
from rest_framework import viewsets, status
from .serializers import GroupSerializer, TestSerializer, ParticipantSerializer, QuestionSerializer, BossSerializer


class GropViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def list(self, request):
        groups = Group.objects.filter(owner=request.user.id)
        print('user:', request.user)

        groups_serializer = self.serializer_class(groups, many=True)
        return Response(groups_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        serializer.data.owner = request.user.email
        serializer.data.owner_name = request.user.get_full_name()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetGroup(APIView):
    serializer_class = GroupSerializer

    def get(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        group = Group.objects.get(pk=id)
        groups_serializer = self.serializer_class(group)
        return Response(groups_serializer.data)


class GetParticipants(APIView):
    serializer_class = ParticipantSerializer

    def get(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        group = Group.objects.get(pk=id)
        participants = AccountStatistics.objects.filter(groups=group.pk)
        participants_serializer = self.serializer_class(participants, many=True)
        return Response(participants_serializer.data)


class GetTestByGrop(APIView):
    serializer_class = TestSerializer

    def get(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        group = Group.objects.get(pk=id)
        tests = Test.objects.filter(group=group)
        tests_serializer = self.serializer_class(tests, many=True)
        return Response(tests_serializer.data)


class GetAccounts(APIView):
    serializer_class = AccountGetSerializer

    def get(self, request, *args, **kwargs):
        accounts = []
        group_pk = self.kwargs['pk']
        group = Group.objects.get(pk=group_pk)
        all_accounts = AccountStatistics.objects.all()
        participants = all_accounts.filter(groups=group.pk)
        for participant in participants:
            participant_id = participant.account.pk
            account = Account.objects.get(pk=participant_id)
            accounts.append(account)
            print("account", account)
        print(accounts)
        participants_serializer = self.serializer_class(accounts, many=True)
        return Response(participants_serializer.data)


class CreateGroup(APIView):
    serializer_class = GroupSerializer

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                owner=request.user,
                owner_name= f'{request.user.last_name} {request.user.first_name} {request.user.patronymic}'
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['GET', 'POST'])
def DeleteGroup(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    return Response({'Группа удалена'})


@api_view(['GET', 'POST'])
def EditGroup(request, group_id):
    group = Group.objects.get(id=group_id)
    new_name = request.data['new_name']
    new_login = request.data['new_login']
    new_password = request.data['new_password']
    if new_name != '' and new_name != ' ':
        group.group_name = new_name
        if new_login != '' and new_login != ' ':
            group.login = new_login
            if new_password != '' and new_password != ' ':
                group.password = new_password
                group.save()
                return Response({'Группа изменена'})


@api_view(['GET', 'POST'])
def DeleteTest(request, test_id):
    group = Test.objects.get(id=test_id)
    group.delete()
    return Response({'Тест удален'})


class BossViewSet(viewsets.ModelViewSet):
    queryset = Boss.objects.all()
    serializer_class = BossSerializer

    def get(self, request):
        boss = Boss.objects.get(pk=self.kwargs['pk'])
        boss_serializer = self.serializer_class(boss)
        return Response(boss_serializer.data, status=status.HTTP_200_OK)


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def list(self, request):
        tests = Test.objects.filter(owner=request.user.id)
        tests_serializer = self.serializer_class(tests, many=True)
        return Response(tests_serializer.data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        test = Test.objects.get(pk=id)
        test_serializer = self.serializer_class(test)
        return Response(test_serializer.data, status=status.HTTP_200_OK)


class CreateTest(APIView):
    serializer_class = TestSerializer

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                owner=request.user,
                owner_name=f'{request.user.last_name} {request.user.first_name} {request.user.patronymic}',
                boss=Boss.objects.get(pk=request.data['boss']),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateQuestion(APIView):
    serializer_class = QuestionSerializer

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                test=Test.objects.get(pk=request.data['id']),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def DeleteQuestion(request):
    question = Question.objects.get(pk=request.data['id'])
    question.delete()
    return Response({'Вопрос удален'})


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request):
        question = Question.objects.filter(owner=request.user.id)
        question_serializer = self.serializer_class(question, many=True)
        return Response(question_serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        question = Question.objects.filter(test=id)
        question_serializer = self.serializer_class(question, many=True)
        return Response(question_serializer.data, status=status.HTTP_200_OK)