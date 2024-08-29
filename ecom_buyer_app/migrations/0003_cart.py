# Generated by Django 5.0.7 on 2024-08-10 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_buyer_app', '0002_user_profile_pic'),
        ('ecom_seller_app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qunatity', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_seller_app.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_buyer_app.user')),
            ],
        ),
    ]