# Generated by Django 4.2 on 2024-02-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coursedetail', '0001_initial'),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_assignment',
            field=models.ManyToManyField(blank=True, null=True, related_name='lesson_assignment', to='exam.exam'),
        ),
    ]
