# Generated by Django 4.2 on 2024-04-16 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_student_student_mock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_flt',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_mock',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_pt',
        ),
    ]