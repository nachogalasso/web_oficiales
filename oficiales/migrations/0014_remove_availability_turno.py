# Generated by Django 4.1.7 on 2023-04-25 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0013_rename_name_availability_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availability',
            name='turno',
        ),
    ]
