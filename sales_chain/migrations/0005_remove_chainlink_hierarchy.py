# Generated by Django 4.2.1 on 2023-06-05 08:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sales_chain', '0004_rename_product_chainlink_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chainlink',
            name='hierarchy',
        ),
    ]