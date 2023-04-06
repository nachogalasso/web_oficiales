# Generated by Django 4.1.7 on 2023-04-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficiales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewRecruits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('surname', models.CharField(max_length=150, null=True)),
                ('email', models.CharField(max_length=150, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='oficiales',
            name='email',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='oficiales',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='oficiales',
            name='phone',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
