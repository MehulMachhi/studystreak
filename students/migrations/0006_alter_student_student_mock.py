# Generated by Django 4.2 on 2024-02-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_alter_exam_exam_category'),
        ('students', '0005_student_student_mock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_mock',
            field=models.ManyToManyField(blank=True, null=True, related_name='mock', to='exam.exam'),
        ),
    ]