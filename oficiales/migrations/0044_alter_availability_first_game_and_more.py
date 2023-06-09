# Generated by Django 4.1.7 on 2023-05-04 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0043_alter_availability_first_game_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='first_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_game', to='oficiales.time'),
        ),
        migrations.AlterField(
            model_name='availability',
            name='second_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_game', to='oficiales.time'),
        ),
    ]
