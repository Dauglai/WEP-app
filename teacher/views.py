from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.forms import modelformset_factory
from .models import Test, Question
from .forms import TestForm, QuestionsForm

"""
class QuestionListView(ListView):
    model = Question
    template_name = "question_list.html"


class QuestionAddView(TemplateView):
    template_name = "add_question.html"

    def get(self, *args, **kwargs):
        formset = QuestionFormSet(queryset=Question.objects.none())
        return self.render_to_response({'question_formset': formset})

    def post(self, *args, **kwargs):
        formset = QuestionFormSet(data=self.request.POST)
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("teacher"))

        return self.render_to_response({'question_formset': formset})
"""

def index(request):
    return render(request, 'main/index.html')


def teacher_office(request):
    return render(request, 'teacher/teacher.html')


def constructor(request):
    error = ''
    if request.method == "POST":
        test_form = TestForm(request.POST)
        if test_form.is_valid():
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


def task(request):
    test = Test.objects.filter(title="Тестовый тест")
    questions = Question.objects.filter(test__title="Тестовый тест")
    return render(request, 'teacher/task1.html', {'tests': test, 'questions': questions})


def questions(request):
    """Session.objects.get(pk=id)"""
    """передача extra через JS"""
    error=''
    QuestionFormSet = modelformset_factory(
        Question,
        fields=('question', 'first_answer', 'second_answer', 'third_answer', 'four_answer','number_correct_answer'),
        extra=2)
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

