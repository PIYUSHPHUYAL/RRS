# Generated by Django 5.0.3 on 2024-04-06 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='type',
            field=models.CharField(default=None),
        ),
    ]
