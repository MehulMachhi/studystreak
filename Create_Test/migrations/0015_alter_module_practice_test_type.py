# Generated by Django 4.2 on 2024-03-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Create_Test', '0014_module_practice_test_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='practice_test_type',
            field=models.CharField(blank=True, choices=[('Reading', 'Reading'), ('Listening', 'Listening'), ('Speaking', 'Speaking'), ('Writing', 'Writing'), ('awa', 'awa'), ('integrated_reasoning', 'integrated_reasoning'), ('verbal_reasoning', 'verbal_reasoning'), ('quantitative_reasoning', 'quantitative_reasoning')], default='Reading', max_length=50, null=True),
        ),
    ]
