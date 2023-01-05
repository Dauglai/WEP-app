from django.urls import path, include
from . import views
from .views import QuestionAddView

urlpatterns = [
    path('', views.teacher_office, name='teacher'),
    path('constructor', views.constructor, name="constructor"),
    path('questions', QuestionAddView.as_view(), name="questions"),
    path('task', views.task, name="task"),
]