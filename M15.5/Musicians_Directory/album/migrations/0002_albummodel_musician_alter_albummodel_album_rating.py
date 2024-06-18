# Generated by Django 5.0.6 on 2024-06-18 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='albummodel',
            name='musician',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musician.musicianmodel'),
        ),
        migrations.AlterField(
            model_name='albummodel',
            name='album_rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
