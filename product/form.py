from re import A
from django.forms import ImageField, ModelForm, TextInput, ModelChoiceField, Form
from django import forms
from .models import Category, Products, Sales, Purchases, Supplier
from django_select2.forms import ModelSelect2Widget


class MyChoiceField(forms.ChoiceField):
    widget = forms.Select(attrs={"required": False})


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["category_name", "category_image"]
        widgets = {
            "category_name": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Catergory Name"}
            ),
            # 'category_id':TextInput(attrs={
            #     C
            #     'placeholder':'Enter Code'
            # }),
            # 'category_image':TextInput(attrs={
            #     "type":"file",
            #    'class':"form-control image-file",
            #    'placeholder':'Enter Code'
            # }
            # )
        }


class AddProductForm(ModelForm):
    class MyForm(forms.ModelForm):
        unit_id = MyChoiceField(
            choices=Products.unit_name,
            widget=forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        )

    class Meta:
        model = Products
        fields = [
            "product_image",
            "product_name",
            "category_id",
            "quantity_in_stock",
            "unit_price",
            "new_stock",
            "cost",
            "reorder_level",
            "unit_of_measure",
            "brand",
            "export_csv",
            "description",
            "supplier",
        ]

        widgets = {
            "product_code": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Code",
                    "data-errors": "Please Enter Code.",
                    "required": "required",
                }
            ),
            "product_name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Name",
                    "data-errors": "Please Enter Name.",
                    "required": "required",
                }
            ),
            "unit_in_stock": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Unit in Stock",
                }
            ),
            "unit_price": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Unit Price",
                }
            ),
            "cost": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Cost",
                }
            ),
            "reorder_level": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Reorder Level",
                }
            ),
            "new_stock": TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "quantity_in_stock": TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            # "category_id":ModelChoiceField(queryset=Category.objects.all(), to_field_name="type")
        }

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields["category_id"].queryset = Category.objects.order_by("category_name")


class FileUploadForm(Form):
    file = forms.FileField()


class AddSalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = [
            "product",
            "quantity",
            "price",
            "discount",
            "date_sold",
        ]


class AddPurchaseForm(ModelForm):
    class Meta:
        model = Purchases
        fields = [
            "product",
            "quantity",
            "purchase_price",
            "purchase_date",
            "supplier",
        ]
