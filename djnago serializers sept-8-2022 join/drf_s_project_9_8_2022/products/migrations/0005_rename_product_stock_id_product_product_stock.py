# Generated by Django 4.1.1 on 2022-09-09 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_stock_id',
            new_name='product_stock',
        ),
    ]
