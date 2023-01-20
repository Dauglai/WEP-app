from django.urls import path, include

from main.views import TestDetailView, Student
from . import views
from .views import TestListView

urlpatterns = [
    path('', views.student, name='student'),
    # path('', Student.as_view(), name='student'),
    # path('student/<slug:slug>/', TestDetailView.as_view(), name='task'),
    path('task', views.task, name="task"),
]