# Generated by Django 4.2.4 on 2023-11-28 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_merge_20231128_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='bio',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 10, 54, 10, 578533)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 10, 54, 10, 578533)),
        ),
    ]
