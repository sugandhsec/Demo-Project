# Generated by Django 5.0.7 on 2024-08-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_seller_app', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
