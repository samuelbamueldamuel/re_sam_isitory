# Generated by Django 4.2.3 on 2023-08-04 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0020_team_team_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
