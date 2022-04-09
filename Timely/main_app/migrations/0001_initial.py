# Generated by Django 4.0.3 on 2022-04-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timezones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timezone', models.CharField(max_length=100)),
                ('hour_toggle', models.BooleanField(default=False)),
                ('availability_start_time', models.CharField(default='00:00', max_length=100)),
                ('availability_end_time', models.CharField(default='23:59', max_length=100)),
            ],
        ),
    ]
