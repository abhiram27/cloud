# Generated by Django 4.2.7 on 2023-11-09 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0004_file_created_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 9, 22, 31, 16, 160113, tzinfo=datetime.timezone.utc)),
        ),
    ]
