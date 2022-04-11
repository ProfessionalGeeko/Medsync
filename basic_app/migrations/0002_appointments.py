# Generated by Django 3.0.3 on 2021-05-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('doctor', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=20)),
                ('time', models.TimeField(max_length=20)),
                ('date', models.DateField(max_length=20)),
            ],
        ),
    ]
