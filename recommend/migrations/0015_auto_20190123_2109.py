# Generated by Django 2.1.5 on 2019-01-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0014_listen_app_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listen',
            name='app_user',
        ),
        migrations.AddField(
            model_name='listen',
            name='app_user',
            field=models.ManyToManyField(to='recommend.AppUser'),
        ),
    ]
