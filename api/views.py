from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView
from product.models import Products
from .serializers import ProductsSerializers
from django_filters.rest_framework import DjangoFilterBackend
import django_filters as filters


class ProductFilter(filters.FilterSet):
    product_name = filters.CharFilter(
        field_name="product_name", lookup_expr="icontains"
    )
    product_code = filters.CharFilter(
        field_name="product_code", lookup_expr="icontains"
    )

    class Meta:
        model = Products
        fields = ["product_code", "product_name"]


class ProductsListApiView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


class ProductsUpdateView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    lookup_field = "pk"


class ProductsFilter(ListAPIView):
    queryset = Products.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = ProductsSerializers
    filterset_class = ProductFilter
    # filter_backends = [filters.SearchFilter]
    # filterset_fields = ["product_code",'product_name']
