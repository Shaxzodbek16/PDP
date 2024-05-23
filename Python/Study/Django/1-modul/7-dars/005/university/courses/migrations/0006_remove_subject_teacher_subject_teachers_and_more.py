# Generated by Django 5.0.4 on 2024-04-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_teacher_degree_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.AddField(
            model_name='subject',
            name='teachers',
            field=models.ManyToManyField(to='courses.teacher'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.RemoveField(
            model_name='subject',
            name='specialities',
        ),
        migrations.AddField(
            model_name='subject',
            name='specialities',
            field=models.ManyToManyField(to='courses.speciality'),
        ),
    ]
