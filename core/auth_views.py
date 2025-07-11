from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .schemas import jwt_response_schema


class MyTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        operation_description="Obtain JWT access & refresh tokens.",
        request_body=TokenObtainPairSerializer,
        responses={200: openapi.Response("JWT pair", jwt_response_schema)},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class MyTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        operation_description="Refresh the access token.",
        request_body=TokenRefreshSerializer,
        # Note: TokenRefreshSerializer returns {'access': ...}, no refresh in response
        responses={
            200: openapi.Response(
                "JWT refresh",
                openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "access": openapi.Schema(
                            type=openapi.TYPE_STRING, description="New access token"
                        ),
                    },
                    required=["access"],
                ),
            )
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
