# Generated by Django 5.0.7 on 2024-08-06 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecom_seller_app', '0002_delete_product_delete_seller_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('profile_picture', models.FileField(default='anonymous.jpg', upload_to='seller_user_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, default='def_pro.jpg', upload_to='product_images/')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('seller_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ecom_seller_app.seller_user')),
            ],
        ),
    ]
