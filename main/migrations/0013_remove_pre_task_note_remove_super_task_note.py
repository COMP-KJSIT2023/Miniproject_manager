# Generated by Django 5.0.4 on 2024-04-06 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_project_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pre_task',
            name='note',
        ),
        migrations.RemoveField(
            model_name='super_task',
            name='note',
        ),
    ]