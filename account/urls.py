from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import RegistrUserView, UserByToken

# router = DefaultRouter()
# router.register(r'registration', RegistrUserView)

urlpatterns = [
    # path('signup/', views.registration, name='signup'),
    path('registr/', RegistrUserView.as_view(), name='registration'),
    path(r'user/by/token/', UserByToken.as_view(), name='login'),
    # path(r'', include(router.urls)),
]
