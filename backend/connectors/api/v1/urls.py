from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134549ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134549", Testconnectors134549ViewSet, basename="testconnectors134549"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
