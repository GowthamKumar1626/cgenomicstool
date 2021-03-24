# Generated by Django 3.0.3 on 2021-03-24 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crosstab', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultmodel',
            name='crosstab_id',
        ),
        migrations.AddField(
            model_name='resultmodel',
            name='job_id',
            field=models.CharField(default='crosstab-20210324-174143-1616607703-061739', max_length=200),
        ),
        migrations.AlterField(
            model_name='ipaddressmodel',
            name='job_id',
            field=models.CharField(default='crosstab-R20210324-174143-1616607703-061739', max_length=200, primary_key=True, serialize=False),
        ),
    ]
