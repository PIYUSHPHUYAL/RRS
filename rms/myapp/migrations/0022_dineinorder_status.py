# Generated by Django 5.0.3 on 2024-04-15 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_dineinorder_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='dineinorder',
            name='status',
            field=models.CharField(default='Preparing', max_length=20),
        ),
    ]
