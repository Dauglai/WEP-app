from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('protagonist/', views.protagonist, name='protagonist'),
    path('task/<int:task_id>/<int:id>/', views.task, name='task'),
    path('watch_group/<int:id>/', views.watch_group, name='watch_group'),
    path('delete_group/<int:id>/', views.delete_group, name='delete_group'),
    path('record/<int:task_id>/', views.task_record, name='record'),
]