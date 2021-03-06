# Generated by Django 2.0 on 2020-03-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0012_auto_20200318_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operatorwindow',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='operatorwindow',
            name='frequency_of_machine_stop',
        ),
        migrations.RemoveField(
            model_name='operatorwindow',
            name='machine_breakdown_time',
        ),
        migrations.RemoveField(
            model_name='operatorwindow',
            name='machine_run_time',
        ),
        migrations.RemoveField(
            model_name='operatorwindow',
            name='machine_stop_time',
        ),
        migrations.RemoveField(
            model_name='operatorwindow',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='operatorwindow',
            name='stop_time',
        ),
        migrations.AddField(
            model_name='operatorwindow',
            name='maintenance_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='operatorwindow',
            name='maintenance_start_time',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='operatorwindow',
            name='maintenance_stop_time',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='operatorwindow',
            name='maintenance_value',
            field=models.CharField(default='', max_length=50),
        ),
    ]
