from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('teacher/', views.teacher_office, name='teacher'),
    path('student/', views.student_office, name='student'),
    # path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
]