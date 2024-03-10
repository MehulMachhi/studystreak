# Generated by Django 4.2 on 2024-03-10 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0006_alter_badge_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='next_badge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gamification.badge'),
        ),
    ]
