from django.contrib import admin
from .models import *

# Register your models here.
class UniversiteAdmin(admin.ModelAdmin):
    list_display = ['code','name','email','contact']
    search_fields = ['name']


class SexeAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']


class UFRAdmin(admin.ModelAdmin):
    list_display = ['code','name','email','contact','universite']
    search_fields = ['name']

class FiliereAdmin(admin.ModelAdmin):
    list_display = ['code','name','ufr']
    search_fields = ['name']


class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ['code','name','filiere']
    search_fields = ['name']


class NiveauAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

class VilleAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

class CommuneAdmin(admin.ModelAdmin):
    list_display = ['name','ville']
    search_fields = ['name']

class Niveau_SpecialiteAdmin(admin.ModelAdmin):
    list_display = ['niveau','specialite']
    search_fields = ['niveau']


class EtudiantAdmin(admin.ModelAdmin):
    list_display = ['name','prenom','lieu_de_naissance','date_de_naissance','sexe','matricule','email','contact','ce','cni','oni','niveau','specialite','universite','ufr','filiere','ville','commune','date']
    search_fields = ['niveau']

admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Niveau_Specialite, Niveau_SpecialiteAdmin)
admin.site.register(Commune, CommuneAdmin)
admin.site.register(Ville, VilleAdmin)
admin.site.register(Niveau, NiveauAdmin)
admin.site.register(Specialite, SpecialiteAdmin)
admin.site.register(Filiere, FiliereAdmin)
admin.site.register(UFR, UFRAdmin)
admin.site.register(Sexe, SexeAdmin)
admin.site.register(Universite, UniversiteAdmin)

