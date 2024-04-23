# Generated by Django 5.0.3 on 2024-04-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_staff_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order123',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.JSONField()),
                ('pickup_time', models.DateTimeField()),
                ('pickup_location', models.CharField(max_length=255)),
                ('order_number', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Order11',
        ),
    ]
