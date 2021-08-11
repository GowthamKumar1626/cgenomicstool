# Generated by Django 3.2.5 on 2021-08-11 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import results.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultsModel',
            fields=[
                ('result_id', models.CharField(default=results.models.result_id_generator, max_length=200, primary_key=True, serialize=False)),
                ('upload_results', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ResultsModel',
                'ordering': ('-created_at',),
            },
        ),
    ]
