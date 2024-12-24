# Generated by Django 4.2.6 on 2023-12-03 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.CharField(max_length=150)),
                ("name", models.CharField(max_length=150)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="c_images/"),
                ),
                ("description", models.TextField(max_length=500)),
                (
                    "status",
                    models.BooleanField(default=False, help_text="0=default,1=Hidden"),
                ),
                (
                    "trending",
                    models.BooleanField(
                        default=False, help_text="0=default,1=Trending"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="shipping_details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=10)),
                ("address", models.TextField(max_length=150)),
                ("state", models.CharField(max_length=50)),
                ("pincode", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.CharField(max_length=150)),
                ("name", models.CharField(max_length=150)),
                (
                    "product_image",
                    models.ImageField(blank=True, null=True, upload_to="p_images/"),
                ),
                ("small_description", models.CharField(max_length=150)),
                ("quantity", models.IntegerField()),
                ("description", models.TextField(max_length=150)),
                ("original_price", models.FloatField()),
                ("selling_price", models.FloatField()),
                (
                    "status",
                    models.BooleanField(default=False, help_text="0=default,1=Hidden"),
                ),
                (
                    "trending",
                    models.BooleanField(
                        default=False, help_text="0=default,1=Trending"
                    ),
                ),
                ("tag", models.CharField(max_length=150)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Ecommerce_app.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CartItems",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=0)),
                (
                    "products",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cartitem",
                        to="Ecommerce_app.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
