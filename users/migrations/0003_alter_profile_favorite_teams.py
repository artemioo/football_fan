# Generated by Django 4.1.7 on 2023-03-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_rename_teams_team'),
        ('users', '0002_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorite_teams',
            field=models.ManyToManyField(blank=True, null=True, related_name='fav_teams', to='teams.team'),
        ),
    ]
