from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('protagonist/', views.protagonist, name='protagonist'),
    path('task/<int:task_id>/', views.task, name='task'),
    path('watchGroup/<int:id>/', views.watchGroup),
    path('deleteGroup/<int:id>/', views.deleteGroup),
]