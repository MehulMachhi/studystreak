# Generated by Django 4.2 on 2024-06-03 05:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_alter_student_active_tokens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='active_tokens',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=list, size=2),
        ),
    ]