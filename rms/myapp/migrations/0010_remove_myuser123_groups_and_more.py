# Generated by Django 5.0.3 on 2024-03-29 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_myuser123_groups_myuser123_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser123',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='myuser123',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='myuser123',
            name='user_permissions',
        ),
    ]