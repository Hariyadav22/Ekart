# Generated by Django 4.2.4 on 2023-12-12 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0005_rename_order_items_shipping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='order',
            new_name='Shipping',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shipping',
            name='id_default',
            field=models.BooleanField(default=False),
        ),
    ]