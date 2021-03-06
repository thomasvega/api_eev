# Generated by Django 3.1.1 on 2020-10-12 13:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20201007_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participate',
            old_name='event',
            new_name='events',
        ),
        migrations.RenameField(
            model_name='participate',
            old_name='user',
            new_name='users',
        ),
        migrations.AlterUniqueTogether(
            name='participate',
            unique_together={('events', 'users')},
        ),
    ]
