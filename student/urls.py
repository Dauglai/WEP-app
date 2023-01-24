from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('task/<int:task_id>/', views.task, name='task'),
]