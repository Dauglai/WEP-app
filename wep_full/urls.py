from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from teacher.urls import router as teacher_router
# from account.urls import router as account_router

router = DefaultRouter()
router.registry.extend(teacher_router.registry)
# router.registry.extend(account_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),

    path('auth/', include('djoser.urls')),
    path('auth-token/', include('djoser.urls.authtoken')),

    path(r'api/account/', include('account.urls')),
    path(r'api/teacher/', include('teacher.urls')),
    path(r'api/student/', include('student.urls')),
]
