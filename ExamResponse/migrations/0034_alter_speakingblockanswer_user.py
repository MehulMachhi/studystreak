# Generated by Django 4.2 on 2024-04-20 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_student_student_flt_student_student_mock_and_more'),
        ('ExamResponse', '0033_alter_speakingblockanswer_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speakingblockanswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
    ]
