from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView, ListCreateAPIView
from product.models import Products, Sales
from .serializers import ProductsSerializers,SalesSerializers
from django_filters.rest_framework import DjangoFilterBackend
import django_filters as filters
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from authentication.models import CustomUser


class ProductFilter(filters.FilterSet):
    # product_name = filters.CharFilter(
    #     field_name="product_name", lookup_expr="icontains"
    # )
    # product_code = filters.CharFilter(
    #     field_name="product_code", lookup_expr="icontains"
    # )
    q = filters.CharFilter(method="filter_q")

    def filter_q(self, queryset, name, value):
        return queryset.filter(
            Q(product_name__icontains=value) | Q(product_code__icontains=value)
        )

    class Meta:
        model = Products
        # fields = ["product_code", "product_name"]
        fields = []


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



class ProductsSales(ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class =SalesSerializers
    def post(self, request, *args, **kwargs):
        sales_data = request.data
        for value in sales_data:
            try:
                quantity = int(value["quantity"])
                product_uuid = value["product_code"]
                total_price = (int(value["sales_price"])) * int(quantity) - int(value["discount"])
                discount = value["discount"]
                price = int(value["sales_price"])
                username = value['user']
                data_sold = value["date_sold"]
                user = CustomUser.objects.get(username=username)

                product = Products.objects.get(product_code=product_uuid)

                if int(product.quantity_in_stock) < int(quantity):
                    print("Not enough stock")
                    message = "Not enough stock"
                    return Response({"data": message}, status=400)

                Sales.objects.create(
                    user=user,
                    product=product,
                    quantity=quantity,
                    total=total_price,
                    discount=discount,
                    price=price,
                    date_sold=data_sold,
                    
                )
            except Exception as e:
                print(e)
                return Response({"error": str(e)}, status=400)

        return Response({"message": "Sales created successfully"}, status=status.HTTP_201_CREATED)
        
        # print(sales_data)
        # # for sales in salse_data:
            
        # return self.create(request, *args, **kwargs)
