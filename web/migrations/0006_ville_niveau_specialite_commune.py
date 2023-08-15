# Generated by Django 4.1.7 on 2023-06-06 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_niveau'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20, verbose_name='Libellé')),
            ],
            options={
                'verbose_name_plural': 'Ville',
            },
        ),
        migrations.CreateModel(
            name='Niveau_Specialite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.niveau', verbose_name='niveau')),
                ('specialite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.specialite', verbose_name='specialite')),
            ],
            options={
                'verbose_name_plural': 'Niveau_Specialite',
            },
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nom')),
                ('ville', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ville', verbose_name='ville')),
            ],
            options={
                'verbose_name_plural': 'Commune',
            },
        ),
    ]