# Generated by Django 3.0.3 on 2021-03-28 19:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crosstab', '0011_auto_20210328_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddressmodel',
            name='expires_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 19, 58, 0, 95743, tzinfo=utc)),
        ),
    ]
