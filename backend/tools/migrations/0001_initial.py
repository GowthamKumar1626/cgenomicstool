# Generated by Django 3.2.5 on 2021-08-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToolsModel',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('image', models.FileField(upload_to='images')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'ToolModel',
                'ordering': ('name',),
            },
        ),
    ]
