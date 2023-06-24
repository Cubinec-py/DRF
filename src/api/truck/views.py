from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema

from src.api.truck.models import Truck
from src.api.truck.serializers import TruckSerializer


@extend_schema(
    tags=['Truck'],
    description='Edit truck information',
    methods=['PATCH'],
    request=TruckSerializer,
    responses={200: TruckSerializer}
)
class TruckViewSet(viewsets.ModelViewSet):
    http_method_names = ['patch']
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    # permission_classes = [permissions.IsAuthenticated]
