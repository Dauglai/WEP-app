from django.urls import path, include

from main.views import TestDetailView, Student
from . import views
from .views import TestListView

urlpatterns = [
    # path('student', views.student_office, name='student'),
    # path('rating_table', views.rating_table, name="rating_table"),
    # path('student/<int:pk>/', TestDetailView.as_view(), name='task'),
    # path('student/<slug:slug>/', TestDetailView.as_view(), name='task'),
    # path('', TestDetailView.as_view(), name="student"),
    path('', Student.as_view(), name='student'),
    # path('student/<slug:slug>/', TestDetailView.as_view(), name='task'),
    path('task', views.task, name="task"),
]