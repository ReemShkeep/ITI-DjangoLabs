# Generated by Django 4.1.7 on 2023-04-01 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='first name', max_length=50, null=True)),
                ('lname', models.CharField(default='last Name', max_length=50, null=True)),
                ('age', models.IntegerField()),
                ('city', models.CharField(default='New Capital', max_length=200, null=True)),
                ('studensTrack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.track')),
            ],
        ),
    ]
