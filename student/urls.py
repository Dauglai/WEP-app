from django.urls import path, include
from . import views

urlpatterns = [
    path('student', views.student_office, name='student'),
    path('', views.student_office, name="student"),
    path('rating_table', views.rating_table, name="rating_table"),
    # path('task', views.task, name="task"),
]