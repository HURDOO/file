# Generated by Django 2.0.13 on 2022-08-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='temporary',
            field=models.BooleanField(default=False),
        ),
    ]
