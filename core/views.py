from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post, User

from .serializers import RegisterSerializer, PostSerializer
from .permissions import IsAuthorOrAdmin

from drf_yasg.utils import swagger_auto_schema
from .schemas import register_response_schema
from drf_yasg import openapi


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Create a new user account.",
        request_body=RegisterSerializer,
        responses={
            201: openapi.Response("User created", register_response_schema),
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAuthorOrAdmin()]
        return [IsAuthenticated()]
