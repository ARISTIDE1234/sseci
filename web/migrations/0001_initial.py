# Generated by Django 4.1.7 on 2023-05-12 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Universite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True, verbose_name='Code')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nom')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='Email')),
                ('contact', models.CharField(max_length=50, unique=True, verbose_name='Contact')),
            ],
            options={
                'verbose_name': 'Nom des universités',
            },
        ),
    ]
