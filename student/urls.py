from django.urls import path, include
from . import views
from .views import TestListView

urlpatterns = [
    # path('student', views.student_office, name='student'),
    # path('', views.student_office, name="student"),
    path('', TestListView.as_view(), name="student"),
    # path('rating_table', views.rating_table, name="rating_table"),
    # path('task', views.task, name="task"),
]