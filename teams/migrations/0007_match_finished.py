# Generated by Django 4.1.7 on 2023-03-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_team_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='finished',
            field=models.BooleanField(default=0),
        ),
    ]
