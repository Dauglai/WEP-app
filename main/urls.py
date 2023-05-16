from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main import views
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    # path(r'', views.index, name='index'),
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('', views.index, name='main'),
# ]
