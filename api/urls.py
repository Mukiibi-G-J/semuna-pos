from django.urls import path
from .views import ProductsListApiView,ProductsUpdateView, ProductsFilter


app_name = "api"


urlpatterns = [
    path("products/", ProductsListApiView.as_view(), name="products"),
    path("products/update/<int:pk>", ProductsUpdateView.as_view(), name="products-update"),
    path("products/filter/", ProductsFilter.as_view(), name="products-filter")
    ]
