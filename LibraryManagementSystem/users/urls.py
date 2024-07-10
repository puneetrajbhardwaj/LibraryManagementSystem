from django.urls import path,include
from .views import UserViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewset)

urlpatterns = [
    path('', include(router.urls)),
]