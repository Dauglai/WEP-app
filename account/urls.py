from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import RegistrUserView, UserByToken

# router = DefaultRouter()
# router.register(r'account', AccountViewSet)

urlpatterns = [
    path('registr/', RegistrUserView.as_view(), name='registration'),
    path(r'user/by/token/', UserByToken.as_view(), name='login'),
    # path(r'', include(router.urls)),
]
