# Generated by Django 4.1.7 on 2023-04-26 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0019_alter_availability_turno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='partido1',
            new_name='partido',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='partido2',
        ),
    ]
