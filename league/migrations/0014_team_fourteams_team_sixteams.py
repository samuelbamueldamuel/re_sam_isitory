# Generated by Django 4.2.1 on 2023-07-22 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0013_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='fourTeams',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='sixTeams',
            field=models.IntegerField(default=0),
        ),
    ]
