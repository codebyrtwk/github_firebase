from django.urls import path, include
from rest_framework import routers
from .views import RepositoryViewSet

router = routers.DefaultRouter()
router.register(r'repositories', RepositoryViewSet, basename='repository')
# router.register(r'users' , UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]