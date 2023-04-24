from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.views.generic import ListView, TemplateView, FormView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.forms import modelformset_factory, NumberInput, TextInput, Textarea, inlineformset_factory
from django.http import HttpResponseRedirect, HttpResponseNotFound

from accounts.models import Account
from .models import Test, Question
from .forms import TestForm, QuestionFormSet, GroupFrom, Question_InlineFormset


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
def teacher(request):
    if not request.user.is_teacher and not request.user.is_staff and not request.user.is_admin:
        return redirect('main')
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


def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    scales = request.POST.getlist("scales", -1)
    if scales == -1:
        return redirect('/teacher/')
    for id in scales:
        group = request.user.group_set.all()

    print(scales)
    return redirect('/teacher/')


def constructor(request):
    if not request.user.is_teacher and not request.user.is_staff and not request.user.is_admin:
        return redirect('main')
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

    test_form = TestForm()
    data = {
        'test_form': test_form,
        'error': error
    }

    return render(request, 'teacher/constructor.html', data)


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


def questions_edit(request, id):
    test = Test.objects.get(pk=id)
    if request.method == "POST":
        formset = Question_InlineFormset(data=request.POST, instance=test)
        if formset.is_valid():
            questions = formset.save(commit=False)
            for question in questions:
                question.test = test
                question.save()
            return redirect("teacher")
    formset = Question_InlineFormset(instance=test)
    return render(request,
        "teacher/questions_edit.html",
        {'question_formset': formset,
        'test_id': id})


def test_delete(request, id):
    try:
        test = Test.objects.get(id=id)
        test.delete()
        return redirect('teacher')
    except Test.DoesNotExist:
        return HttpResponseNotFound("<h2>Test not found</h2>")


def question_delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return redirect('questions')
