# Generated by Django 3.2.5 on 2021-07-23 17:22

from django.db import migrations, models
import results.models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_auto_20210723_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultsmodel',
            name='result_id',
            field=models.CharField(default=results.models.result_id_generator, max_length=200, primary_key=True, serialize=False),
        ),
    ]