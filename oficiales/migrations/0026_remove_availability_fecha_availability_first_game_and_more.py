# Generated by Django 4.1.7 on 2023-05-02 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0025_alter_calendar_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availability',
            name='fecha',
        ),
        migrations.AddField(
            model_name='availability',
            name='first_game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_game', to='oficiales.calendar'),
        ),
        migrations.AddField(
            model_name='availability',
            name='second_game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_game', to='oficiales.calendar'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='horario',
            field=models.CharField(choices=[('13hs', '13hs'), ('15.30hs', '15.30hs')], max_length=100, null=True),
        ),
    ]