# Generated by Django 4.2 on 2024-02-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_alter_exam_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='block_type',
            field=models.CharField(blank=True, choices=[('Assignments', 'Assignments'), ('Mock Test', 'Mock Test')], max_length=200, null=True),
        ),
    ]
