# Generated by Django 5.1.3 on 2024-11-19 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_quantity',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
