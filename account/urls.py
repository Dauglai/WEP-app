from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import RegistrUserView

# router = DefaultRouter()
# router.register(r'registration', RegistrUserView)

urlpatterns = [
    # path('signup/', views.registration, name='signup'),

    # path('api-auth', include('rest_framework.urls')),
    # path('auth/', include('djoser.urls')),
    path('registr/', RegistrUserView.as_view(), name='registr'),
    # path(r'', include(router.urls)),
]
