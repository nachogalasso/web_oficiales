# Generated by Django 4.1.7 on 2023-05-29 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0057_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('team_logo', models.ImageField(null=True, upload_to='')),
                ('team', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='oficiales.teams')),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=True, null=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oficiales.games')),
                ('oficial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oficiales.oficiales')),
            ],
        ),
        migrations.CreateModel(
            name='Designaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('R', 'R'), ('U', 'U'), ('HL', 'HL'), ('LJ', 'LJ'), ('SJ', 'SJ'), ('FJ', 'FJ'), ('BJ', 'BJ')], max_length=10, null=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oficiales.games')),
                ('oficiales', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oficiales.oficiales')),
            ],
        ),
    ]
