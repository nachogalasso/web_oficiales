# Generated by Django 4.1.7 on 2023-05-04 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0037_rename_horario_calendar_game_rename_name_time_turno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='game',
        ),
        migrations.RemoveField(
            model_name='time',
            name='fecha',
        ),
        migrations.AddField(
            model_name='calendar',
            name='horario',
            field=models.ManyToManyField(to='oficiales.time'),
        ),
        migrations.AlterField(
            model_name='availability',
            name='first_game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_game', to='oficiales.time'),
        ),
        migrations.AlterField(
            model_name='availability',
            name='second_game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_game', to='oficiales.time'),
        ),
    ]