from django.urls import path, include
from . import views

urlpatterns = [
    # path('signup/', views.registration, name='signup'),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
]
