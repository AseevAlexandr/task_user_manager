# Generated by Django 5.1.3 on 2024-11-18 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='task_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Пользователь '),
            preserve_default=False,
        ),
    ]
