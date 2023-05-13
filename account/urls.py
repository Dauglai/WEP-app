from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.registration, name='signup'),
]
