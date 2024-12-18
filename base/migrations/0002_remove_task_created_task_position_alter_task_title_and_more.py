# Generated by Django 5.1.3 on 2024-12-02 07:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
        migrations.AddField(
            model_name='task',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
