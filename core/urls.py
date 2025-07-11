from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterAPIView, PostViewSet

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("", include(router.urls)),
]
