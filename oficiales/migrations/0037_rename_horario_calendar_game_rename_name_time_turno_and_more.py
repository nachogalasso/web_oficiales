# Generated by Django 4.1.7 on 2023-05-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0036_rename_available_availability_partido1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendar',
            old_name='horario',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='name',
            new_name='turno',
        ),
        migrations.RemoveField(
            model_name='calendar',
            name='fecha',
        ),
        migrations.AddField(
            model_name='time',
            name='fecha',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
