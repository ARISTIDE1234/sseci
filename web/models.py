from django.db import models
from django.utils import timezone

# Create your models here.
class Universite(models.Model):
    code=models.CharField('Code',unique=True,max_length=15)
    name=models.CharField('Nom',unique=True,max_length=150)
    email=models.EmailField('Email',unique=True,max_length=100)
    contact=models.CharField('Contact',unique=True,max_length=50)
    
    class Meta:
        verbose_name_plural = 'Nom des universités'

    def __str__(self):
        return self.name
    

    
class Sexe(models.Model):
    libelle=models.CharField('Libellé',max_length=20)
    
    class Meta:
        verbose_name_plural = 'Sexe'

    def __str__(self):
        return self.libelle
    


class UFR(models.Model):
    code=models.CharField('Code',unique=True,max_length=15)
    name=models.CharField('Nom',unique=True,max_length=150)
    email=models.EmailField('Email',unique=True,max_length=100)
    contact=models.CharField('Contact',unique=True,max_length=50)
    universite=models.ForeignKey(Universite, verbose_name='Université',on_delete = models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Nom des UFR'

    def __str__(self):
        return self.name
    

class Filiere(models.Model):
    code=models.CharField('Code',unique=True,max_length=15)
    name=models.CharField('Nom',unique=True,max_length=150)
    ufr=models.ForeignKey(UFR, verbose_name='Ufr',on_delete = models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Nom des Filières'

    def __str__(self):
        return self.name
    

class Specialite(models.Model):
    code=models.CharField('Code',unique=True,max_length=15)
    name=models.CharField('Nom',unique=True,max_length=150)
    filiere=models.ForeignKey(Filiere, verbose_name='filiere',on_delete = models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Nom des Spécialités'

    def __str__(self):
        return self.name
    
class Niveau(models.Model):
    libelle=models.CharField('Libellé',max_length=20)
    
    class Meta:
        verbose_name_plural = 'Niveau'

    def __str__(self):
        return self.libelle
    
class Ville(models.Model):
    libelle=models.CharField('Libellé',max_length=20)
    
    class Meta:
        verbose_name_plural = 'Ville'

    def __str__(self):
        return self.libelle
    

class Commune(models.Model):
    name=models.CharField('Nom',unique=True,max_length=150)
    ville=models.ForeignKey(Ville, verbose_name='ville',on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Commune'

    def __str__(self):
        return self.libelle
    

class Niveau_Specialite(models.Model):
    niveau=models.ForeignKey(Niveau, verbose_name='niveau',on_delete = models.CASCADE)
    specialite=models.ForeignKey(Specialite, verbose_name='specialite',on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Niveau_Specialite'

    def __str__(self):
        return self.libelle
    


class Etudiant(models.Model):
    name=models.CharField('Nom',max_length=150)
    prenom=models.CharField('Prenom',max_length=150)
    lieu_de_naissance=models.CharField('Lieu de naissance',max_length=150)
    date_de_naissance=models.DateField('Date de naissance')
    matricule=models.CharField('Matricule',unique=True,max_length=15)
    email=models.EmailField('Email',unique=True,max_length=100)
    contact=models.CharField('Contact',unique=True,max_length=50)
    ce=models.FileField('Carte etudiante',upload_to="carte_ce",max_length=150)
    cni=models.CharField('Numéro CNI',unique=True,max_length=15)
    oni=models.FileField('Pièce nationale d\'identité',upload_to="carte_cni",max_length=150)
    universite=models.ForeignKey(Universite, verbose_name='Université',on_delete = models.CASCADE)
    sexe=models.ForeignKey(Sexe, verbose_name='Sexe',on_delete = models.CASCADE)
    ufr=models.ForeignKey(UFR, verbose_name='Ufr',on_delete = models.CASCADE)
    specialite=models.ForeignKey(Specialite, verbose_name='Specialite',on_delete = models.CASCADE)
    filiere=models.ForeignKey(Filiere, verbose_name='Filiere',on_delete = models.CASCADE)
    niveau=models.ForeignKey(Niveau, verbose_name='Niveau',on_delete = models.CASCADE)
    ville=models.ForeignKey(Ville, verbose_name='Ville',on_delete = models.CASCADE)
    commune=models.ForeignKey(Commune, verbose_name='Commune',on_delete = models.CASCADE)
    date=models.DateTimeField('Date d\'identification',default=timezone.now)

    class Meta:
        verbose_name_plural = 'Etudiant'

    def __str__(self):
        return self.name
