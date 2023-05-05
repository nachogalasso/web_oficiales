# Generated by Django 4.1.7 on 2023-05-02 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0026_remove_availability_fecha_availability_first_game_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availability',
            name='date_informed',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='first_game',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='partido1',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='partido2',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='second_game',
        ),
        migrations.AddField(
            model_name='availability',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='availability',
            name='calendar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oficiales.calendar'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='horario',
            field=models.CharField(max_length=100, null=True),
        ),
    ]