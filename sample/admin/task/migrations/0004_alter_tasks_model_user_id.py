# Generated by Django 4.1.13 on 2024-01-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_tasks_model_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks_model',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
