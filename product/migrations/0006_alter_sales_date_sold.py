# Generated by Django 5.0.4 on 2024-05-10 04:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0005_order_staff_sales_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sales",
            name="date_sold",
            field=models.DateField(blank=True, null=True),
        ),
    ]