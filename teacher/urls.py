from django.template.context_processors import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teacher import views

from .views import GropViewSet, TasksViewSet, CreateGroup, GetGroup, GetParticipants, GetAccounts, \
    GetTestByGrop, QuestionViewSet, BossViewSet, CreateTest, CreateQuestion

router = DefaultRouter()
router.register(r'groups', GropViewSet)
router.register(r'tests', TasksViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'boss', BossViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'create_group/', CreateGroup.as_view(), name='createGroup'),
    path('get_group/<int:pk>/', GetGroup.as_view(), name='getGroup'),
    path('get_participants/<int:pk>/', GetParticipants.as_view(), name='getParticipants'),
    path('get_accounts/<int:pk>/', GetAccounts.as_view(), name='getAccounts'),

    path('get_tests_by_group/<int:pk>/', GetTestByGrop.as_view(), name='getAccounts'),
    path('delete_group/<int:group_id>', views.DeleteGroup, name='delete_group'),
    path('edit_group/<int:group_id>', views.EditGroup, name='edit_group'),

    path(r'create_test/', CreateTest.as_view(), name='createTest'),
    path('delete_test/<int:test_id>', views.DeleteTest, name='delete_test'),

    path('create_question/', CreateQuestion.as_view(), name='createQuestion'),
    path('delete_question/', views.DeleteQuestion, name='delete_question'),
]
