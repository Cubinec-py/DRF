from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema

from src.api.cargo.models import Cargo
from src.api.cargo.serializers import CargoSerializer


@extend_schema(
    tags=['Cargo'],
    description='Cargo information and cargo edit',
    methods=['POST', 'GET', 'PATCH', 'DELETE'],
    request=CargoSerializer,
    responses={200: CargoSerializer}
)
class CargoViewSet(viewsets.ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    # permission_classes = [permissions.IsAuthenticated]
