# Generated by Django 4.1.6 on 2023-03-11 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0012_remove_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='extras',
        ),
    ]
