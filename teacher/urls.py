from django.urls import path, re_path
from . import views
from .views import QuestionAddView

urlpatterns = [
    path('', views.teacher, name='teacher'),
    path('constructor/', views.constructor, name="constructor"),
    path('questions/', QuestionAddView.as_view(), name="questions"),
]