# Generated by Django 4.2.7 on 2023-12-30 08:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_alter_bill_time_alter_post_time_alter_product_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 15, 28, 17, 10434)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 15, 28, 17, 11434)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 15, 28, 17, 10434)),
        ),
    ]
