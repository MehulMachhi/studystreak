# Generated by Django 4.2 on 2024-02-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_alter_exam_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='examblockaudio/'),
        ),
    ]