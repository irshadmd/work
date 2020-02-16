# Generated by Django 3.0.3 on 2020-02-16 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='operator_attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_id', models.CharField(default='', max_length=5)),
                ('operator_name', models.CharField(default='', max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('attendence', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
