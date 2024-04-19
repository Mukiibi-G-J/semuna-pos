from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView
from product.models import Products
from .serializers import ProductsSerializers


class ProductsListApiView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


class ProductsUpdateView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    lookup_field = "pk"
