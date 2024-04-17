# Generated by Django 5.0.1 on 2024-03-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_super_task_note_task_note_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pre_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateField(default=None, null=True)),
                ('task_heading', models.CharField(max_length=20)),
                ('task_details', models.CharField(max_length=500)),
                ('weightage', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('note', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
    ]
