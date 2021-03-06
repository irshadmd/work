# Generated by Django 2.0 on 2020-03-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0002_auto_20200303_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatorwindow',
            name='duration',
            field=models.TimeField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='operatorwindow',
            name='machine_breakdown_time',
            field=models.TimeField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='operatorwindow',
            name='machine_run_time',
            field=models.TimeField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='operatorwindow',
            name='machine_stop_time',
            field=models.TimeField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='operatorwindow',
            name='start_time',
            field=models.TimeField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='operatorwindow',
            name='stop_time',
            field=models.TimeField(default='', max_length=50),
        ),
    ]
