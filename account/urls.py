from django.urls import path
from .views import RegistrUserView, UserByToken, CreateStatistics

# router = DefaultRouter()
# router.register(r'account', AccountViewSet)

urlpatterns = [
    path('registr/', RegistrUserView.as_view(), name='registration'),
    path('create-statistics/', CreateStatistics.as_view(), name='create-statistics'),
    path(r'user/by/token/', UserByToken.as_view(), name='login'),
    # path(r'', include(router.urls)),
]
