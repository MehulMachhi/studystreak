# Generated by Django 4.2 on 2024-02-22 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_alter_exam_exam_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_type',
            field=models.CharField(blank=True, choices=[('Reading', 'Reading'), ('Listening', 'Listening'), ('Speaking', 'Speaking'), ('Writing', 'Writing'), ('General', 'General'), ('a_w_a', 'a_w_a'), ('integrated_reasoning', 'integrated_reasoning'), ('quantitative_reasoning', 'quantitative_reasoning'), ('verbal_reasoning', 'verbal_reasoning')], default='Reading', help_text='(Reading, Listening, Speaking, Writing)', max_length=200, null=True),
        ),
    ]