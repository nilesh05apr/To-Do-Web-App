# Generated by Django 4.0 on 2022-01-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('True', 'complete'), ('False', 'incomplete')], default='False', max_length=10),
        ),
    ]
