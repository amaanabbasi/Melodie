# Generated by Django 2.1.5 on 2019-01-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0011_auto_20190123_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default='', upload_to='albums'),
        ),
    ]
