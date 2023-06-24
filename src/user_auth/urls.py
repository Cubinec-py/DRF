from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.user_auth.views import SignUpView, CustomTokenObtainPairView, CustomTokenRefreshView


router = DefaultRouter()
router.register(r'registration', SignUpView, basename='registration')


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair', kwargs={"swagger_name": "Authorization"}),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]
