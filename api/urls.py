from django.urls import path
from .views import ProductsListApiView,ProductsUpdateView


app_name = "api"


urlpatterns = [
    path("products/", ProductsListApiView.as_view(), name="products"),
    path("products/update/<int:pk>", ProductsUpdateView.as_view(), name="products-update")
    ]
