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

class TeacherTestListView(ListView):
    model = Test
    template_name = 'teacher/teacher.html'

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

