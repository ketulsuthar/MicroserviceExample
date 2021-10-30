from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializers


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, requrst, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass