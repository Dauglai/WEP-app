from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.teacher_office, name='teacher'),
    path('constructor', views.constructor, name="constructor"),
    path('task', views.task, name="task"),
]