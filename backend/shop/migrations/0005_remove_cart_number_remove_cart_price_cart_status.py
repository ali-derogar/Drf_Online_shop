# Generated by Django 4.1.3 on 2023-06-16 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_cart_product_cart_user_category_parent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='number',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
