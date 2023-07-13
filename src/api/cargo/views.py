from rest_framework import viewsets, permissions
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from api.cargo.models import Cargo
from api.cargo.serializers import (
    CargoSerializer,
    MyParametersSerializer,
    PatchCargoSerializer,
)


@extend_schema(
    tags=["Cargo"],
    description="Cargo information and cargo edit",
    methods=["POST", "GET", "DELETE"],
    request=CargoSerializer,
    responses={200: CargoSerializer},
)
@extend_schema(tags=["Cargo"], methods=["PATCH"], request=PatchCargoSerializer)
class CargoViewSet(viewsets.ModelViewSet):
    http_method_names = ["post", "get", "patch", "delete"]
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    @extend_schema(
        methods=["GET"],
        parameters=[
            OpenApiParameter(
                name="weight", location=OpenApiParameter.QUERY, required=False, type=int
            ),
            OpenApiParameter(
                name="trucks_near",
                location=OpenApiParameter.QUERY,
                required=False,
                type=int,
            ),
        ],
    )
    def list(self, request):
        serializer = MyParametersSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        weight = validated_data.get("weight", None)
        trucks_near = validated_data.get("trucks_near", None)
        if weight:
            self.queryset = self.queryset.filter(weight=int(weight))
        if trucks_near:
            for cargo in self.queryset:
                cargo.trucks_near = trucks_near
        serializer = CargoSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Cargo.objects.filter(pk=pk)
        for query in queryset:
            query.trucks_near = 10000
        serializer = CargoSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses={
            204: None,
            404: {
                "description": "The object was not found.",
                "example": {"detail": "Cargo not found"},
            },
        }
    )
    def destroy(self, request, pk=None):
        if Cargo.objects.filter(pk=pk).exists():
            Cargo.objects.filter(pk=pk).delete()
            return Response(status=204)
        return Response(status=404, data={"detail": "Cargo not found"})
