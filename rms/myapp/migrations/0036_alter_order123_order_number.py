# Generated by Django 5.0.3 on 2024-05-13 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_alter_order123_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order123',
            name='order_number',
            field=models.IntegerField(unique=True),
        ),
    ]
