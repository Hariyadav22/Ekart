# Generated by Django 4.2.6 on 2023-12-06 05:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Ecommerce_app", "0003_order_items_orders_delete_shipping_details"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orders",
            name="Quantity",
        ),
        migrations.RemoveField(
            model_name="orders",
            name="price",
        ),
    ]
