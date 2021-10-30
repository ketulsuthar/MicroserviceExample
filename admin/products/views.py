import random

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializers


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            print(product)
            serializer = ProductSerializers(product)
            return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ProductSerializers(instance=product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):

    def get(self, _):
        try:
            users = User.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            if len(users):
                user = random.choice(users)
                return Response({
                    'id': user.id
                })
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)