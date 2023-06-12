from django.urls import path
from main import views

urlpatterns = [
    path('', views.index),

    path('main', views.index, name='main'),
    path('login/', views.index, name='login'),
    path('registration/', views.index, name='login'),
    path('task/details/<int:id>/', views.index, name='login'),

    path('teacher/profile/', views.index),
    path('teacher/statistics/', views.index, ),
    path('teacher/statistics-teacher/', views.index),
    path('teacher/constructor/task-constructor/', views.index),
    path('teacher/constructor/questions-constructor/', views.index),
    path('teacher/group/list/', views.index),
    path('teacher/group/details/<id>/', views.index),
    path('teacher/task/list/', views.index),
    path('teacher/group/details/<id>/', views.index),

    path('student/main/', views.index),
    path('student/profile/', views.index),
    path('student/statistics/', views.index, ),
    path('student/group/list/', views.index),
    path('student/group/details/<id>/', views.index),
    path('student/task/list/', views.index),
]
