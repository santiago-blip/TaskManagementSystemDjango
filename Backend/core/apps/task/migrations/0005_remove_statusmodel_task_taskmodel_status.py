# Generated by Django 4.2.7 on 2023-11-24 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_categorymodel_task_alter_statusmodel_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statusmodel',
            name='task',
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='status',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.statusmodel'),
        ),
    ]
