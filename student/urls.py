from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import GropViewSet, GetTestByGrop

router = DefaultRouter()
router.register(r'groups', GropViewSet)
router.register(r'tests-by-group', GetTestByGrop)

urlpatterns = [
    path(r'', include(router.urls)),

    # path('', views.student, name='student'),
    # path('protagonist/', views.protagonist, name='protagonist'),
    # path('task/<int:task_id>/', views.task, name='task'),
    # path('watch_group/<int:id>/', views.watch_group, name='watch_group'),
    # path('delete_group/<int:id>/', views.delete_group, name='delete_group'),
]