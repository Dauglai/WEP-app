from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.views.generic import ListView, TemplateView, FormView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.forms import modelformset_factory, NumberInput, TextInput, Textarea, inlineformset_factory
from django.http import HttpResponseRedirect, HttpResponseNotFound
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Account
from student.models import Account_Statistics
from .decorators import access_teacher
from .models import Test, Question, Group
from .forms import TestForm, QuestionFormSet, GroupFrom, Question_InlineFormset, RewardStudent, UpdateGroupForm


from rest_framework import viewsets, status, authentication
from .serializers import GroupSerializer, TestsSerializer


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
        print(request.user)
        serializer = GroupSerializer(data=request.data)
        serializer.data.owner = request.user.email
        serializer.data.owner_name = request.user.get_full_name()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestsSerializer

    def list(self, request):
        # tests = request.user.test_set.all()
        tests = Test.objects.filter(owner=request.user.id)
        print('user:', request.user)

        tests_serializer = self.serializer_class(tests, many=True)
        return Response(tests_serializer.data, status=status.HTTP_200_OK)


# class GropView(ListModelMixin, GenericAPIView):
#     serializer_class = GroupSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         return Group.objects.filter(owner=pk)
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
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


# from .serializers import QuestionSerializer, AnswerSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response


# class GetQuestion(GenericAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = QuestionSerializer
#
#     def get(self, request, format=None):
#         questions = Question.objects.all()
#         last_point = QuestionSerializer(questions, many=True)
#         return Response(last_point.data)
#
#
# class QuestionAnswer(GenericAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = AnswerSerializer
#
#     def post(self, request, format=None):
#         answer = AnswerSerializer(data=request.data, context=request)
#         if answer.is_valid(raise_exception=True):
#             answer.save()
#             return Response({'result': 'OK'})

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

# @access_teacher
# def question_delete(request, question_id):
#     print(question_id)
#     question = Question.question.get(pk=question_id)
#     if request.method == "POST":
#         question.delete()
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@access_teacher
def test_delete(request, id):
    try:
        test = Test.objects.get(id=id)
        test.delete()
        return redirect('teacher')
    except Test.DoesNotExist:
        return HttpResponseNotFound("<h2>Test not found</h2>")


@access_teacher
def question_delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return redirect('questions')


@access_teacher
def edit_group(request, group_id):
    group = Group.objects.get(id=group_id)

    if str(request.user.email) != str(group.owner):
        return redirect('main')

    if request.method == 'POST':
        form = UpdateGroupForm(request.POST)
        if form.is_valid():
            new_name = form.data.get('new_name')
            new_login = form.data.get('new_login')
            new_password = form.data.get('new_password')
            if new_name != '' and new_name != ' ':
                group.group_name = new_name
            if new_login != '' and new_login != ' ':
                group.login = new_login
            if new_password != '' and new_password != ' ':
                group.password = new_password
            group.save()
            return redirect('teacher')

    update_form = UpdateGroupForm(initial={
        'new_name': group.group_name,
        'new_login': group.login,
        'new_password': group.password,
    })
    data = {
        'group': group,
        'update_form': update_form,
    }
    return render(request, 'teacher/edit_group.html', context=data)


@access_teacher
def view_group(request, group_id):
    group = Group.objects.get(id=group_id)

    if str(request.user.email) != str(group.owner):
        return redirect('main')

    if request.method == "POST":
        participant = request.POST.get('participant')
        reward = int(request.POST.get("reward"))
        student = Account_Statistics.objects.get(pk=participant)
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
    all_accounts = Account_Statistics.objects.all()
    participants = all_accounts.filter(groups=group)

    data = {
        'reward_form': reward_form,
        'group': group,
        'participants': participants,
    }
    return render(request, 'teacher/view_group.html', context=data)


@access_teacher
def delete_participant(request, group_id, student_id):
    participant = Account_Statistics.objects.get(pk=student_id)
    group = Group.objects.get(id=group_id)
    try:
        participant.groups.remove(group)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Account_Statistics.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@access_teacher
def delete_group(request, group_id):
    group = Group.objects.get(id=group_id)

    if str(request.user.email) != str(group.owner):
        return redirect('main')

    group.delete()
    return redirect('teacher')
