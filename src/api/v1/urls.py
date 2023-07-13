from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.cargo.views import CargoViewSet
from api.truck.views import TruckViewSet

router = DefaultRouter()

router.register("cargo", CargoViewSet, basename="cargo")
router.register("truck", TruckViewSet, basename="truck")

urlpatterns = [
    path("", include(router.urls)),
]
