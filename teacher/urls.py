from django.urls import path, re_path
from . import views
from .views import QuestionAddView, QuestionEditView

urlpatterns = [
    path('', views.teacher, name='teacher'),
    path("postuser/", views.postuser),
    path('test/new/', views.constructor, name="constructor"),
    path('questions/', QuestionAddView.as_view(), name="questions"),
    path("test/edit/<int:id>/", views.test_edit, name='test_edit'),
    path("test/delete/<int:id>/", views.test_delete, name='test_delete'),
    path("delete/<int:id>/", views.question_delete, name='question_delete'),
    path("questions/edit/<id>", views.questions_edit, name='questions_edit'),
]