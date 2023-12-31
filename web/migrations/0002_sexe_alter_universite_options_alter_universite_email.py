# Generated by Django 4.1.7 on 2023-05-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sexe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20, verbose_name='Libellé')),
            ],
            options={
                'verbose_name_plural': 'Sexe',
            },
        ),
        migrations.AlterModelOptions(
            name='universite',
            options={'verbose_name_plural': 'Nom des universités'},
        ),
        migrations.AlterField(
            model_name='universite',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='Email'),
        ),
    ]
