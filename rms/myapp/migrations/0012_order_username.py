# Generated by Django 5.0.3 on 2024-03-29 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
