# Generated by Django 4.1.7 on 2023-04-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0005_alter_student_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]
