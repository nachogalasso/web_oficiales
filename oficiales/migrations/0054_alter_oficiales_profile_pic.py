# Generated by Django 4.1.7 on 2023-05-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0053_alter_reviews_play_numb_alter_reviews_player_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficiales',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user_logo_nbg.png', null=True, upload_to=''),
        ),
    ]