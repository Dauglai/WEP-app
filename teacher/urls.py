from django.urls import path, include

from main.views import Teacher
from . import views
from .views import QuestionAddView

urlpatterns = [
    path('', Teacher.as_view(), name='teacher'),
    path('constructor', views.constructor, name="constructor"),
    path('questions', QuestionAddView.as_view(), name="questions"),
]