# Generated by Django 4.2.1 on 2023-06-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sales_chain', '0002_alter_chainlink_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chainlink',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
