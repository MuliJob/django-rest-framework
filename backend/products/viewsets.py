"""Product ViewSets"""
from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """Product ViewSets"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    """Product ViewSets"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
