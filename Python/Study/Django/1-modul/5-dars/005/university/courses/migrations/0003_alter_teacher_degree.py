# Generated by Django 5.0.4 on 2024-04-20 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='degree',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4')], max_length=10),
        ),
    ]
