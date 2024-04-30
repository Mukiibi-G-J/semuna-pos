from django.urls import path
from .views import ProductsListApiView,ProductsUpdateView, ProductsFilter,ProductsSales


app_name = "api"


urlpatterns = [
    path("products/", ProductsListApiView.as_view(), name="products"),
    path("products/update/<int:pk>", ProductsUpdateView.as_view(), name="products-update"),
    path("products/filter/", ProductsFilter.as_view(), name="products-filter"),
    path("products/sales/", ProductsSales.as_view(), name="products_sales")
    ]
