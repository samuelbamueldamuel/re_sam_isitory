# Generated by Django 4.2.3 on 2023-08-04 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0021_alter_team_team_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_salary',
        ),
        migrations.CreateModel(
            name='TeamSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_salary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.team')),
            ],
        ),
    ]