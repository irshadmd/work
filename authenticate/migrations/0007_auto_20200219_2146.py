# Generated by Django 2.0 on 2020-02-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0006_operator_skill_matrix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='operator_id',
            field=models.CharField(default='', max_length=5, primary_key=True, serialize=False),
        ),
    ]