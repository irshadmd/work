# Generated by Django 3.0.3 on 2020-02-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_auto_20200211_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatorWindow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_id', models.CharField(default='', max_length=5)),
                ('operator_name', models.CharField(default='', max_length=50)),
                ('operation', models.CharField(default='', max_length=100)),
                ('start_time', models.TimeField()),
                ('stop_time', models.TimeField()),
                ('duration', models.TimeField()),
                ('date', models.DateField()),
                ('machine_stop_time', models.TimeField()),
                ('machine_run_time', models.TimeField()),
                ('machine_breakdown_time', models.TimeField()),
                ('frequency_of_machine_stop', models.IntegerField(default=0)),
                ('ticket_no_start', models.IntegerField(default=0)),
                ('ticket_no_end', models.IntegerField(default=0)),
                ('total_pieces', models.IntegerField(default=0)),
                ('ticket_no_run_time', models.IntegerField(default=0)),
                ('next_ticket_no_time', models.IntegerField(default=0)),
                ('ct', models.CharField(default='', max_length=50)),
                ('total_stitched_pieces', models.IntegerField(default=0)),
                ('rework_ticket_no', models.IntegerField(default=0)),
                ('rework_pieces', models.IntegerField(default=0)),
            ],
        ),
    ]
