# Generated by Django 2.2 on 2019-08-24 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('max_equipos', models.IntegerField()),
                ('descr', models.CharField(max_length=300)),
                ('timestamp', models.BigIntegerField()),
                ('id_pulso', models.BigIntegerField()),
                ('listo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('id_grupo', models.IntegerField()),
                ('id_torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randomTorneo.Torneo')),
            ],
        ),
    ]
