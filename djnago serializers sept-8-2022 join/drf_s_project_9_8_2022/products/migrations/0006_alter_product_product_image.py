# Generated by Django 4.1.1 on 2022-09-09 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_product_stock_id_product_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to='products/'),
        ),
    ]