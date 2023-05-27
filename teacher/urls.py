from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teacher import views

from .views import GropViewSet, TasksViewSet, CreateGroup, GetGroup, GetParticipants, GetAccounts, \
    GetTestByGrop, QuestionViewSet

router = DefaultRouter()
router.register(r'groups', GropViewSet)
router.register(r'tests', TasksViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'create_group/', CreateGroup.as_view(), name='createGroup'),
    path('get_group/<int:pk>/', GetGroup.as_view(), name='getGroup'),
    path('get_participants/<int:pk>/', GetParticipants.as_view(), name='getParticipants'),
    path('get_accounts/<int:pk>/', GetAccounts.as_view(), name='getAccounts'),
    path('get_tests_by_group/<int:pk>/', GetTestByGrop.as_view(), name='getAccounts'),
    path('delete_group/<int:group_id>', views.DeleteGroup, name='delete_group'),
    path('edit_group/<int:group_id>', views.EditGroup, name='edit_group'),


    path('delete_test/<int:test_id>', views.DeleteTest, name='delete_test'),

    # path('group/', GropView.as_view(), name='group'),

    # path('test/new/', views.constructor, name="constructor"),
    # path('questions/', QuestionAddView.as_view(), name="questions"),
    #
    # path("test/edit/<int:id>/", views.test_edit, name='test_edit'),
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
