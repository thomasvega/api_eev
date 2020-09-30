# Generated by Django 3.1.1 on 2020-09-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_module'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='events',
        ),
        migrations.AddField(
            model_name='event',
            name='modules',
            field=models.ManyToManyField(to='api.Module'),
        ),
    ]