# Generated by Django 4.1.7 on 2023-04-16 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0009_calendar_horario_alter_calendar_local_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.CharField(max_length=100, null=True)),
                ('play_numb', models.IntegerField()),
                ('penalty_code', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(choices=[('Super Mal', 'Super Mal'), ('Mal', 'Mal'), ('Bien', 'Bien'), ('Muy Bien', 'Muy Bien'), ('Excelente', 'Excelente'), ('?', '?')], max_length=50)),
                ('official', models.CharField(choices=[('R', 'R'), ('U', 'U'), ('HL', 'HL'), ('LJ', 'LJ'), ('SJ', 'SJ'), ('FJ', 'FJ'), ('BJ', 'BJ')], max_length=50, null=True)),
                ('official_name', models.CharField(max_length=100, null=True)),
                ('team', models.CharField(choices=[('Corsarios', 'Corsarios'), ('Cruzados', 'Cruzados'), ('Jabalies', 'Jabalies'), ('Legionarios', 'Legionarios'), ('Osos Polares', 'Osos Polares'), ('Tiburones', 'Tiburones')], max_length=100, null=True)),
                ('comments', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='availability',
            name='game2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oficiales.calendar'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='horario',
            field=models.CharField(choices=[('1er partido - 13hs', '1er partido - 13hs'), ('2do partido - 15.30hs', '2do partido - 15.30hs')], max_length=100, null=True),
        ),
    ]
