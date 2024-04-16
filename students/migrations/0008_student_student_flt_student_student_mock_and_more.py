# Generated by Django 4.2 on 2024-04-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Create_Test', '0017_alter_module_practice_test_type'),
        ('exam', '0015_alter_exam_exam_category'),
        ('students', '0007_remove_student_student_flt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_flt',
            field=models.ManyToManyField(blank=True, null=True, to='Create_Test.fulllengthtest'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_mock',
            field=models.ManyToManyField(blank=True, null=True, related_name='mock', to='exam.exam'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_pt',
            field=models.ManyToManyField(blank=True, null=True, related_name='+', to='Create_Test.createexam'),
        ),
    ]
