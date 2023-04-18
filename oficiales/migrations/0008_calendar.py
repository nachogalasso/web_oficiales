# Generated by Django 4.1.7 on 2023-04-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0007_rename_status_availability_partido1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('local', models.CharField(choices=[('Corsarios', 'Corsarios'), ('Cruzados', 'Cruzados'), ('Jabalies', 'Jabalies'), ('Legionarios', 'Legionarios'), ('Osos Polares', 'Osos Polares'), ('Tiburones', 'Tiburones')], max_length=100)),
                ('visitante', models.CharField(choices=[('Corsarios', 'Corsarios'), ('Cruzados', 'Cruzados'), ('Jabalies', 'Jabalies'), ('Legionarios', 'Legionarios'), ('Osos Polares', 'Osos Polares'), ('Tiburones', 'Tiburones')], max_length=100)),
            ],
        ),
    ]