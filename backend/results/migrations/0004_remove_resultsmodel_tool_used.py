# Generated by Django 3.2.5 on 2021-07-25 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_alter_resultsmodel_result_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultsmodel',
            name='tool_used',
        ),
    ]