# Generated by Django 4.2.7 on 2023-11-10 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0009_alter_file_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='deleted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
