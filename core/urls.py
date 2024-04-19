from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django_select2 import urls as select2_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("product.urls", namespace="products")),
    path("auth/", include("authentication.urls", namespace="authentication")),
    path("select2/", include(select2_urls), name="select2"),
]


urlpatterns += [path("api/", include("api.urls", namespace="api"))]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    

