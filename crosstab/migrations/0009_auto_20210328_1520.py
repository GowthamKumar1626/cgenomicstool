# Generated by Django 3.0.3 on 2021-03-28 15:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crosstab', '0008_auto_20210328_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddressmodel',
            name='expires_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 15, 20, 2, 925163, tzinfo=utc)),
        ),
    ]