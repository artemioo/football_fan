# Generated by Django 4.1.7 on 2023-03-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=220),
        ),
    ]