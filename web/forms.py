from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model=Etudiant
        fields= (
        'name','prenom','lieu_de_naissance','date_de_naissance','matricule','email','contact','ce','cni','oni','universite','sexe','ufr','specialite','filiere','niveau','ville','Commune'
        )
    
widgets={
    'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Nom'}),
    'pronom': forms.TextInput(attrs={'class':'form-control','placeholder':'Prénom'}),
    'lieu_de_naissance': forms.TextInput(attrs={'class':'form-control','placeholder':'Lieu de naissance'}),
    'date_de_naissance': forms.DateInput(attrs={'class':'form-control','placeholder':'Date de naissance'}),
    'sexe': forms.Select(attrs={'class':'form-control','placeholder':'Sexe'}),
    'matricule': forms.TextInput(attrs={'class':'form-control','placeholder':'Matricule'}),
    'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
    'contact': forms.TextInput(attrs={'class':'form-control','placeholder':'Contact'}),
    'ce': forms.FileInput(attrs={'class':'form-control','placeholder':'Carte etudiante'}),
    'cni': forms.TextInput(attrs={'class':'form-control','placeholder':'Numéro CNI'}),
    'oni': forms.FileInput(attrs={'class':'form-control','placeholder':'Pièce nationale d\'identité'}),
    'universite': forms.Select(attrs={'class':'form-control','placeholder':'Université'}),
    'ufr': forms.Select(attrs={'class':'form-control','placeholder':'Ufr'}),
    'specialite': forms.Select(attrs={'class':'form-control','placeholder':'Spécialité'}),
    'filiere': forms.Select(attrs={'class':'form-control','placeholder':'Filiere'}),
    'niveau': forms.Select(attrs={'class':'form-control','placeholder':'Niveau'}),
    'ville': forms.Select(attrs={'class':'form-control','placeholder':'Ville'}),
    'commune': forms.Select(attrs={'class':'form-control','placeholder':'Commune'}),
}

