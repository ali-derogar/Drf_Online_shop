# Generated by Django 4.1.3 on 2023-06-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='number',
            field=models.IntegerField(),
        ),
    ]
