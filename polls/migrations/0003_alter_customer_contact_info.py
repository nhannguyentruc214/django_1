# Generated by Django 5.1.3 on 2024-11-19 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_product_stock_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contact_info',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]