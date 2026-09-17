from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
from .views import BookViewSet, home
urlpatterns = [
    path('', include(router.urls)),
]