from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('teacher', views.teacher_office, name='teacher'),
    path('student', views.student_office, name='student'),
    path('constructor', views.constructor, name='constructor')
]