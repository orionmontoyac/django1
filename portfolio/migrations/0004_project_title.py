# Generated by Django 2.0.2 on 2020-03-27 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='Title', max_length=200),
        ),
    ]
