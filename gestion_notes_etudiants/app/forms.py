from django import forms
from .models import Etudiant, Ue, Ressource, Examen, Note, Enseignant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        exclude = ['id_etudiant']
        labels = {
            'prenom': 'Prénom',
            'nom': 'Nom',
            'email': 'Email',
            'groupe': 'Groupe',
            'photo': 'Photo de l’étudiant',
        }

class UEForm(forms.ModelForm):
    class Meta:
        model = Ue
        exclude = ['id_ue']
        labels = {
            'nom': 'Nom de l’UE',
            'semestre': 'Semestre',
            'credits': 'Crédits ECTS',
        }

class RessourceForm(forms.ModelForm):
    class Meta:
        model = Ressource
        exclude = ['id_ressource']
        labels = {
            'ue': 'Unité d’enseignement (UE)',
            'nom': 'Nom de la ressource',
            'description': 'Description',
        }

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        exclude = ['id_examen']
        labels = {
            'nom': 'Titre de l’examen',
            'date': 'Date',
            'coefficient': 'Coefficient',
            'id_ressource': 'Ressource associée',
            'id_enseignant': 'Enseignant',
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['id_note']
        labels = {
            'id_etudiant': 'Étudiant',
            'id_examen': 'Examen',
            'note': 'Note obtenue',
            'appreciation': 'Appréciation',
        }

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        exclude = ['id_enseignant']
        labels = {
            'prenom': 'Prénom',
            'nom': 'Nom',
            'email': 'Email',
        }


class ImportCSVForm(forms.Form):
    file = forms.FileField(label="Importer un fichier CSV")