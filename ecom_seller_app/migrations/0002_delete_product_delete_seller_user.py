# Generated by Django 5.0.7 on 2024-08-03 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_seller_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Seller_User',
        ),
    ]
