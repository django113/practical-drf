# Generated by Django 4.1.1 on 2022-09-09 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drf_s_app', '0004_alter_choice_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drf_s_app.question'),
        ),
    ]
