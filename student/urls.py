from django.urls import path, include
from . import views

urlpatterns = [
    # path('student', views.student_office, name='student'),
    path('student', views.student_office, name="student"),
]