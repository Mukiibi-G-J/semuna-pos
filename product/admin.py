from django.contrib import admin
from . import models
from django.db import models as model
from django.shortcuts import render
from django.urls import path, reverse
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from mptt.admin import MPTTModelAdmin
from django import forms

admin.site.site_header = "Semuna POS"


# <------customer filter ------------>
class NewStockFilter(admin.SimpleListFilter):
    title = "New Stock"
    parameter_name = "new_stock"

    def lookups(self, request, model_admin):
        return (
            ("positive", "Greater than zero"),
            ("non_positive", "Zero or less"),
        )

    def queryset(self, request, queryset):
        if self.value() == "positive":
            return queryset.filter(new_stock__gt=0)
        elif self.value() == "non_positive":
            return queryset.filter(new_stock__lte=0)


class StockTakeFilter(admin.SimpleListFilter):
    title = "Stock Count"
    parameter_name = "stock_take_done"

    def lookups(self, request, model_admin):
        return (
            ("No", "Stock Take not done"),
            ("Yes", "Stock take done"),
        )

    def queryset(self, request, queryset):
        if self.value() == "Yes":
            print(self.value())
            print(queryset.filter(stock_take_done=True))
            return queryset.filter(stock_take_done=True)
        elif self.value() == "No":
            return queryset.filter(stock_take_done=False)


# class NoArrowsNumberInput(forms.widgets.NumberInput):
#     template_name = "admin/widgets/no_arrows_number_input.html"


@admin.register(models.Products)
class ModleAdmin(admin.ModelAdmin):
    list_display = (
        "product_code",
        "product_name",
        "unit_price",
        "quantity_in_stock",
        "new_stock",
        "cost",
        "reorder_level",
        "new_arrival",
        "stock_take_done",
    )

    search_fields = (
        "product_code",
        "product_name",
        "quantity_in_stock",
        "stock_take_done",
    )
    order_by = "created_at"
    list_filter = (NewStockFilter, StockTakeFilter)

    # formfield_overrides = {
    #     model.IntegerField: {"widget": NoArrowsNumberInput},
    # }

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.base_fields["quantity_in_stock"].widget = forms.TextInput()
        return form


admin.site.register(models.Brand)
admin.site.register(models.Product_Unit)


# csv upload form
class CategoryAdminCSV(forms.Form):
    csv_upload = forms.FileField()


@admin.register(models.Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ["category_name", "category_image"]

    def upload_csv(self, request):
        form = CategoryAdminCSV()

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            if not csv_file.name.endswith(".csv"):
                messages.waring(request, "the wrong file type was upload")
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            # >>['category_name, 01', 'Bags, 01', 'Bottles, 01', 'Bowls, 01', 'Busengeja, 01', 'Dish, 01', 'Flaskcup, 01', 'Flasks, 01', 'Flying pans, 01', 'Food Flasks, 01']
            print(csv_data)
            for x in csv_data:
                fields = x.split(",")
                created = models.Category.objects.update_or_create(
                    category_name=fields[0]
                )
            url = reverse("admin:index")
            return HttpResponseRedirect(url)
        context = {"form": form}
        return render(request, "admin/csv_upload.html", context)

    # registeting  a a url  to admin site
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv/", self.upload_csv)]
        return new_urls + urls


@admin.register(models.Purchases)
class PurchasesAdmin(admin.ModelAdmin):
    list_display = (
        "get_product_name",
        "quantity",
        "purchase_price",
        "purchase_date",
        "supplier",
        "created_at",
    )
    search_fields = ("product__product_name", "supplier__name")

    def get_product_name(self, obj):
        return obj.product.product_name


@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = (
        "get_product_name",
        "quantity",
        "price",
        "date_sold",
    )
    search_fields = ("product__product_name",)

    list_filter = ("date_sold",)

    def get_product_name(self, obj):
        return obj.product.product_name
