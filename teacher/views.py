from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Account
from account.serializers import AccountGetSerializer
from student.models import AccountStatistics
from .decorators import access_teacher
from .models import Test, Question, Group, Boss
from .forms import TestForm, QuestionFormSet, GroupFrom, Question_InlineFormset, RewardStudent, UpdateGroupForm


from rest_framework import viewsets, status, authentication
from .serializers import GroupSerializer, TestSerializer, ParticipantSerializer, QuestionSerializer, BossSerializer


# <angular>

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
    # authentication_classes = [authentication.TokenAuthentication]
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


def GetTest(APIView):
    serializer_class = TestSerializer
    def get(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        test = Test.objects.get(pk=id)
        test_serializer = self.serializer_class(test)
        return Response(test_serializer.data, status=status.HTTP_200_OK)


# </angular>



class QuestionAddView(TemplateView):
    template_name = 'teacher/questions.html'

    def get(self, *args, **kwargs):
        formset = QuestionFormSet(queryset=Question.objects.none())
        return self.render_to_response({'question_formset': formset})

    def post(self, *args, **kwargs):
        error = ''
        formset = QuestionFormSet(data=self.request.POST)
        test = Test.objects.get(pk=(Test.objects.last()).id)
        # print(formset)
        if formset.is_valid():
            questions = formset.save(commit=False)
            for question in questions:
                question.test = test
                question.save()
            return redirect("teacher")
        else:
            error = 'Форма была неверной'

        formset = QuestionFormSet()
        data = {
            'question_formset': formset,
            'error': error
        }
        return self.render_to_response(data)


class QuestionEditView(TemplateView):
    template_name = 'teacher/questions_edit.html'

    def get(self, *args, **kwargs):
        id = self.request.session['test_id']
        test = Test.objects.get(pk=id)
        formset = QuestionFormSet(instance=test)
        formset.extra = 0
        return self.render_to_response({'question_formset': formset})

    def post(self, *args, **kwargs):
        id = self.request.session['test_id']
        test = Test.objects.get(pk=id)
        error = ''
        formset = QuestionFormSet(data=self.request.POST, instance=test)
        if formset.is_valid():
            questions = formset.save(commit=False)
            for question in questions:
                question.test = test
                question.save()
            return redirect("teacher")
        else:
            error = "Форма была неверной"

        formset = QuestionFormSet(instance=test)
        data = {
            'question_formset': formset,
            'error': error
        }
        return self.render_to_response(data)



@login_required
@access_teacher
def teacher(request):
    error = ''
    tests = request.user.test_set.all()
    groups = request.user.group_set.all()
    # checked_groups = request.user

    if request.method == "POST":
        group_form = GroupFrom(request.POST)
        if group_form.is_valid():
            group_form = group_form.save(commit=False)
            print(group_form.owner)
            group_form.owner = Account.objects.get(pk=(request.user.id))
            group_form.owner_name = f'{request.user.last_name} {request.user.first_name} {request.user.patronymic}'
            group_form.save()
            return redirect('teacher')
        else:
            error = 'Форма была неверной'

    group_form = GroupFrom()
    data = {
        'group_form': group_form,
        'tests': tests,
        'groups': groups,
    }
    return TemplateResponse(request, 'teacher/teacher.html', data)


@access_teacher
def constructor(request):
    error = ''
    if request.method == "POST":
        test_form = TestForm(request.POST)
        print(request.user.email)
        if test_form.is_valid():
            test_form = test_form.save(commit=False)
            test_form.owner = Account.objects.get(pk=(request.user.id))
            test_form.owner_name = f'{request.user.last_name} {request.user.first_name} {request.user.patronymic}'
            print(test_form.owner)
            test_form.save()
            return redirect('questions')
        else:
            error = 'Форма была неверной'

    groups = Group.objects.all()
    test_form = TestForm()
    data = {
        'test_form': test_form,
        'error': error,
        'groups': groups
    }

    return render(request, 'teacher/constructor.html', data)


@access_teacher
def test_edit(request, id):
    test = Test.objects.get(pk=id)
    if request.method == "POST":
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
            request.session['test_id'] = id
            return redirect('questions_edit', id=id)
    test_form = TestForm(instance=test)
    return render(request, "teacher/test_edit.html", {"test_form": test_form})


@access_teacher
def questions_edit(request, id):
    test = Test.objects.get(pk=id)
    questions_set = Test.objects.filter()
    print(questions_set)
    if request.method == "POST":
        formset = Question_InlineFormset(data=request.POST, instance=test)
        if formset.is_valid():
            questions = formset.save(commit=False)
            print(questions)
            for question in questions:
                question.test = test
                question.save()
            return redirect("teacher")
    formset = Question_InlineFormset(instance=test)
    return render(request,
                  "teacher/questions_edit.html",
                  {'question_formset': formset,
                   'test_id': id})


@access_teacher
def question_delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return redirect('questions')



@access_teacher
def view_group(request, group_id):
    group = Group.objects.get(id=group_id)

    if str(request.user.email) != str(group.owner):
        return redirect('main')

    if request.method == "POST":
        participant = request.POST.get('participant')
        reward = int(request.POST.get("reward"))
        student = AccountStatistics.objects.get(pk=participant)
        score = int(student.score)
        print(score)
        if 'replenishment' in request.POST:
            score += reward
        elif 'withdrawal' in request.POST:
            score -= reward
            if score < 0: score = 0
        else:
            print('error view_group')
        student.score = score
        student.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    reward_form = RewardStudent()
    all_accounts = AccountStatistics.objects.all()
    participants = all_accounts.filter(groups=group)

    data = {
        'reward_form': reward_form,
        'group': group,
        'participants': participants,
    }
    return render(request, 'teacher/view_group.html', context=data)


@access_teacher
def delete_participant(request, group_id, student_id):
    participant = AccountStatistics.objects.get(pk=student_id)
    group = Group.objects.get(id=group_id)
    try:
        participant.groups.remove(group)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except AccountStatistics.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
