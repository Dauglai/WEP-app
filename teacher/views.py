from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.forms import modelformset_factory, NumberInput, TextInput, Textarea

from accounts.models import Account
from .models import Test, Question, Choice, Answer
from .forms import TestForm, AnswerForm, QuestionFormSet


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


def index(request):
    return render(request, 'main/index.html')


def teacher_office(request):
    return render(request, 'teacher/teacher.html')

def task(request):
    test = Test.objects.get(pk=(Test.objects.last()).id)
    questions = Question.objects.filter(test__title=test.title)
    data = {
        'test': test,
        'questions': questions
    }
    return render(request, 'teacher/task1.html', data)


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

    test_form = TestForm()
    data = {
        'test_form': test_form,
        'error': error
    }
    return render(request, 'teacher/constructor.html', data)


class QuestionAddView(TemplateView):
    template_name = 'teacher/questions.html'

    def get(self, *args, **kwargs):
        formset = QuestionFormSet(queryset=Question.objects.none())
        return self.render_to_response({'question_formset': formset})

    def post(self, *args, **kwargs):
        error = ''
        formset = QuestionFormSet(data=self.request.POST)
        # print(formset)
        if formset.is_valid():
            questions = formset.save(commit=False)
            for question in questions:
                question.test = Test.objects.get(pk=(Test.objects.last()).id)
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

def questions(request):
    error=''
    QuestionFormSet = modelformset_factory(
        Question,
        fields=('question', 'first_answer', 'second_answer', 'third_answer', 'four_answer', 'reward', 'number_correct_answer'),
        widgets={
            'question': Textarea(attrs={
                'placeholder': "Поле для ввода вопроса",
                'class': "form-control",
                'rows': 2, 'cols': 50,
            }),
            'first_answer': Textarea(attrs={
                'placeholder': "Ответ",
                'class': "answer",
                'rows':1, 'cols':50,
            }),
            'second_answer': Textarea(attrs={
                'placeholder': "Ответ",
                'class': "answer",
                'rows':1, 'cols':50,
            }),
            'third_answer': Textarea(attrs={
                'placeholder': "Ответ",
                'class': "answer",
                'rows':1, 'cols':50,
            }),
            'four_answer': Textarea(attrs={
                'placeholder': "Ответ",
                'class': "answer",
                'rows':1, 'cols':50,
            }),
            'number_correct_answer': NumberInput(attrs={
                'style': 'width:50px',
            }),
            'reward': NumberInput(attrs={
                'style': 'width:50px',
                'value': 1,
            }),
        },
        extra=1)
    """передача extra через JS"""
    formset = QuestionFormSet(data=request.POST)
    if formset.is_valid():
        questions = formset.save(commit=False)
        for question in questions:
            question.test = Test.objects.get(pk=(Test.objects.last()).id)
            question.save()
        return redirect("teacher")
    else:
        error = 'Форма была неверной'

    formset = QuestionFormSet()
    data = {
        'formset': formset,
        'error': error
    }
    return render(request, 'teacher/questions.html', data)

