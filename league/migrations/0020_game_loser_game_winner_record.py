# Generated by Django 4.2.4 on 2023-08-09 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0019_remove_team_fourteams_remove_team_sixteams'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='loser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loser', to='league.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='league.team'),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='league.team')),
            ],
        ),
    ]
