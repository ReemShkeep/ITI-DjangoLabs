# Generated by Django 4.1.7 on 2023-04-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0003_remove_course_trackcourses_track_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='studentsCourse',
            field=models.ManyToManyField(to='iot.course'),
        ),
    ]
