# Generated by Django 4.1.7 on 2023-05-04 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0041_rename_game_calendar_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='first_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_game', to='oficiales.time'),
        ),
    ]