# Generated by Django 4.1.7 on 2023-05-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0045_availability_user_oficiales_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='oficiales',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
