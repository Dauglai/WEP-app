from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import QuestionAddView, GropViewSet, TasksViewSet

router = DefaultRouter()
router.register(r'groups', GropViewSet)
router.register(r'tests', TasksViewSet)

urlpatterns = [
    # path('', views.teacher, name='teacher'),
    path(r'', include(router.urls)),
    # path('group/', GropView.as_view(), name='group'),

    # path('test/new/', views.constructor, name="constructor"),
    # path('questions/', QuestionAddView.as_view(), name="questions"),
    #
    # path("test/edit/<int:id>/", views.test_edit, name='test_edit'),
    # path("test/delete/<int:id>/", views.test_delete, name='test_delete'),
    #
    # path("delete/<int:id>/", views.question_delete, name='question_delete'),
    # path("questions/edit/<id>", views.questions_edit, name='questions_edit'),
    # # path("question_delete/<int: question_id>", views.question_delete, name='question_delete'),
    #
    # path('edit_group/<int:group_id>', views.edit_group, name='edit_group'),
    # path('view_group/<int:group_id>', views.view_group, name='view_group'),
    # path('delete_participant/<int:group_id>/<int:student_id>', views.delete_participant, name='delete_participant'),
    # path('delete_group/<int:group_id>', views.delete_group, name='delete_group'),
]
