# Generated by Django 4.2.3 on 2023-08-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0019_merge_0013_offer_0018_team_fourteams_team_sixteams'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_salary',
            field=models.FloatField(null=True),
        ),
    ]