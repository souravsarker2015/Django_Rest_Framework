# Generated by Django 4.0.1 on 2022-02-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_review_review_user_alter_review_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='num_rating',
            field=models.IntegerField(default=0),
        ),
    ]
