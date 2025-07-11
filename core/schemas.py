from drf_yasg import openapi

# Swagger Api schema for register
register_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "username": openapi.Schema(type=openapi.TYPE_STRING, description="Username"),
        "email": openapi.Schema(
            type=openapi.TYPE_STRING, format="email", description="Email address"
        ),
    },
    required=["username", "email"],
)

# Swagger Api schema for Tokens
jwt_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "refresh": openapi.Schema(
            type=openapi.TYPE_STRING, description="Refresh token"
        ),
        "access": openapi.Schema(type=openapi.TYPE_STRING, description="Access token"),
    },
    required=["refresh", "access"],
)
