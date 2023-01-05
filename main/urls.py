from django.urls import path, include
from django.contrib import admin
from . import views
from .views import TestListView, StatisticListView

urlpatterns = [
    path('', views.index, name='main'),
    path('teacher/', views.teacher_office, name='teacher'),
    path('student/', TestListView.as_view(), name='student'),
    path('rating_table/', StatisticListView.as_view(), name='rating_table'),
    # path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
]