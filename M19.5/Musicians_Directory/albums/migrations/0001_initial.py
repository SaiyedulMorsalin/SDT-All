# Generated by Django 5.0.6 on 2024-07-09 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=150)),
                ('album_rating', models.ImageField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], upload_to='')),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicians.musicianmodel')),
            ],
        ),
    ]
