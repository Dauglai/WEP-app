from django.urls import path

from . import views
from .views import RegistrUserView, UserByToken, CreateStatistics

urlpatterns = [
    path('registr/', RegistrUserView.as_view(), name='registration'),
    path('create-statistics/', CreateStatistics.as_view(), name='create-statistics'),
    path(r'user/by/token/', UserByToken.as_view(), name='login'),
    path('create-hero/', views.CreateHero, name='create-hero'),
]
