# Generated by Django 4.1.7 on 2023-05-10 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0047_remove_teams_name_teams_team_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teams',
            old_name='team',
            new_name='name',
        ),
    ]
