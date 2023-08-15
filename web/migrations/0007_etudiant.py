# Generated by Django 4.1.7 on 2023-06-06 18:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_ville_niveau_specialite_commune'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=150, verbose_name='Prenom')),
                ('lieu_de_naissance', models.CharField(max_length=150, verbose_name='Lieu de naissance')),
                ('date_de_naissance', models.DateField(verbose_name='Date de naissance')),
                ('matricule', models.CharField(max_length=15, unique=True, verbose_name='Matricule')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('contact', models.CharField(max_length=50, unique=True, verbose_name='Contact')),
                ('ce', models.FileField(max_length=150, upload_to='', verbose_name='Carte etudiante')),
                ('cni', models.CharField(max_length=15, unique=True, verbose_name='Numéro CNI')),
                ('oni', models.FileField(max_length=150, upload_to='', verbose_name="Pièce nationale d'identité")),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'identification")),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.commune', verbose_name='Commune')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.filiere', verbose_name='Filiere')),
                ('niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.niveau', verbose_name='Niveau')),
                ('sexe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.sexe', verbose_name='Sexe')),
                ('specialite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.specialite', verbose_name='Specialite')),
                ('ufr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ufr', verbose_name='Ufr')),
                ('universite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.universite', verbose_name='Université')),
                ('ville', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ville', verbose_name='Ville')),
            ],
            options={
                'verbose_name_plural': 'Nom des UFR',
            },
        ),
    ]