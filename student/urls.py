from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import GropViewSet, GetTestByGrop

router = DefaultRouter()
router.register(r'groups', GropViewSet)
router.register(r'tests-by-group', GetTestByGrop)

urlpatterns = [
    path(r'', include(router.urls)),
    path('exclude_group/<int:id>/', views.DeleteGroup, name='delete_group'),
    path('join_group/', views.JoinGroup, name='join_group'),

    # path('', views.student, name='student'),
    # path('protagonist/', views.protagonist, name='protagonist'),
    # path('task/<int:task_id>/', views.task, name='task'),
    # path('watch_group/<int:id>/', views.watch_group, name='watch_group'),
]