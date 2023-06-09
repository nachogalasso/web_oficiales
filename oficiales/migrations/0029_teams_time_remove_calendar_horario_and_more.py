# Generated by Django 4.1.7 on 2023-05-03 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0028_availability_date_informed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='calendar',
            name='horario',
        ),
        migrations.AddField(
            model_name='availability',
            name='horario',
            field=models.ManyToManyField(to='oficiales.time'),
        ),
        migrations.AddField(
            model_name='calendar',
            name='horario',
            field=models.ManyToManyField(to='oficiales.time'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='local',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='local', to='oficiales.teams'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='visitante',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visitante', to='oficiales.teams'),
        ),
    ]
