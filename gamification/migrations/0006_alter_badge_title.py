# Generated by Django 4.2 on 2024-03-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0005_badge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
