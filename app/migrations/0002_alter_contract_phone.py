# Generated by Django 4.0.1 on 2022-01-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='phone',
            field=models.IntegerField(),
        ),
    ]