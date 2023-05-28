from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import GropViewSet, GetTestByGrop, HeroViewSet, ProtagonistViewSet, AccountStatisticsViewSet

router = DefaultRouter()
router.register(r'groups', GropViewSet)
router.register(r'tests-by-group', GetTestByGrop)
router.register(r'hero', HeroViewSet)
router.register(r'protagonist', ProtagonistViewSet)
router.register(r'account_statistics', AccountStatisticsViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path('exclude_group/<int:id>/', views.DeleteGroup, name='delete_group'),
    path('join_group/', views.JoinGroup, name='join_group'),

    # path('protagonist/', views.protagonist, name='protagonist'),
]