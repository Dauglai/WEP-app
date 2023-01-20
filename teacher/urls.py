from django.urls import path, re_path, include

from main.views import Teacher
from . import views
from .views import QuestionAddView, FormGroup

urlpatterns = [
    # path('', Teacher.as_view(), name='teacher'),
    path('', views.teacher, name='teacher'),
    re_path(r'^$', views.index, name='index'),
    path('constructor/', views.constructor, name="constructor"),
    path('questions/', QuestionAddView.as_view(), name="questions"),
]