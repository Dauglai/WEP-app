from django.urls import path, include

from main.views import TestDetailView, Student
from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('task', views.task, name="task"),
]