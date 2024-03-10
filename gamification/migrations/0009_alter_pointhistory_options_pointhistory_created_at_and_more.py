# Generated by Django 4.2 on 2024-03-10 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0008_pointhistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pointhistory',
            options={'verbose_name_plural': 'Point Histories'},
        ),
        migrations.AddField(
            model_name='pointhistory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 3, 10, 10, 23, 11, 208483, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pointhistory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
