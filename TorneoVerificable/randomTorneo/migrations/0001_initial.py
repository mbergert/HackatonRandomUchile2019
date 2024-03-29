# Generated by Django 2.2 on 2019-08-24 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Torneos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('max_equipos', models.IntegerField()),
                ('descripcion', models.CharField(max_length=300)),
                ('timestamp', models.BigIntegerField()),
                ('id_pulso', models.BigIntegerField()),
                ('listo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('id_grupo', models.IntegerField()),
                ('id_torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randomTorneo.Torneos')),
            ],
        ),
    ]
