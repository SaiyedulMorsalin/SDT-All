# Generated by Django 5.0.6 on 2024-06-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicianmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]