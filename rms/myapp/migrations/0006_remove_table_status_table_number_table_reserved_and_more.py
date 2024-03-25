# Generated by Django 5.0.3 on 2024-03-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='status',
        ),
        migrations.AddField(
            model_name='table',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='table',
            name='reserved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='table',
            name='size',
            field=models.IntegerField(),
        ),
    ]
