# Generated by Django 4.2 on 2024-03-17 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursedetail', '0004_note_note_unique_intro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='live_class',
            new_name='lesson',
        ),
    ]
