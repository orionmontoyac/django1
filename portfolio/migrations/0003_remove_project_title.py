# Generated by Django 2.0.2 on 2020-03-27 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
    ]
