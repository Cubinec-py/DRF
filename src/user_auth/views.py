from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user_auth.serializers import SignUpSerializer


@extend_schema(
    tags=['Authorization'],
    description='Obtain token',
    methods=['POST'],
    request=TokenObtainPairSerializer,
    responses={200: TokenObtainPairSerializer}
)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(
    tags=['Authorization'],
    description='Refresh token',
    methods=['POST'],
    request=TokenRefreshSerializer,
    responses={200: TokenRefreshSerializer}
)
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema(
    tags=['Authorization'],
    description='Sign up',
    methods=['POST'],
    request=SignUpSerializer,
    responses={201: SignUpSerializer}
)
class SignUpView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = SignUpSerializer
