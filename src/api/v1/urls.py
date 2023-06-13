from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.cargo.views import CargoViewSet

router = DefaultRouter()

router.register('cargo', CargoViewSet, basename='cargo')

urlpatterns = [
    path('', include(router.urls)),
]
