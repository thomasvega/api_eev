# Generated by Django 3.1.1 on 2020-09-30 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200930_0857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='user',
            new_name='member',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='votes',
        ),
        migrations.AddField(
            model_name='vote',
            name='vote',
            field=models.BooleanField(default='False', verbose_name='Vote'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='participate',
            name='creator',
            field=models.BooleanField(verbose_name=False),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.event')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.member')),
            ],
        ),
    ]