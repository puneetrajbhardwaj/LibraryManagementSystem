from django.urls import path,include
from .views import BookViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewset)

urlpatterns = [
    path('', include(router.urls)),
]