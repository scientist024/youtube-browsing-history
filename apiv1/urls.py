from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, StreamerViewSet


router = routers.DefaultRouter()
router.register(r"movie", MovieViewSet)
router.register(r"streamer", StreamerViewSet)


urlpatterns = [
    path("", include(router.urls))
]
