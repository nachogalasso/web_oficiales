# Generated by Django 4.1.7 on 2023-05-03 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0035_alter_time_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='available',
            new_name='partido1',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='match',
        ),
        migrations.AddField(
            model_name='availability',
            name='first_game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_game', to='oficiales.calendar'),
        ),
        migrations.AddField(
            model_name='availability',
            name='partido2',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='availability',
            name='second_game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_game', to='oficiales.calendar'),
        ),
    ]
