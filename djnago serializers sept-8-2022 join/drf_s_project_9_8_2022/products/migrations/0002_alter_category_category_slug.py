# Generated by Django 4.1.1 on 2022-09-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
