from django.urls import path, include
from django.contrib import admin

from . import views
from .views import StatisticListView, Teacher, Student

urlpatterns = [
    path('', views.index, name='main'),
    path('teacher/', Teacher.as_view(), name='teacher'),
    path('student/', Student.as_view(), name='student'),
    # path('student/<int:pk>/', TestDetailView.as_view(), name='student'),
    path('rating_table/', StatisticListView.as_view(), name='rating_table'),
    # path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
]