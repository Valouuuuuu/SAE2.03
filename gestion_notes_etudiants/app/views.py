from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Etudiant, Ressource, Examen, Note, Enseignant, Ue
from .forms import EtudiantForm, UEForm, RessourceForm, ExamenForm, NoteForm, EnseignantForm, ImportCSVForm
from django.contrib import messages
import csv
from collections import defaultdict

def base(request):
    return render (request, 'base.html')
# Index
def index(request):
    return render(request, 'app/index.html')

# Etudiants
def etudiants(request):
    form = EtudiantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('etudiants'))
    etudiants = Etudiant.objects.all()
    return render(request, 'app/etudiants.html', {'form': form, 'etudiants': etudiants})

def supprimer_etudiant(request, id):
    try:
        Etudiant.objects.get(id_etudiant=id).delete()
    except Etudiant.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('etudiants'))

def modifier_etudiant(request, id):
    try:
        etudiant = Etudiant.objects.get(id_etudiant=id)
    except Etudiant.DoesNotExist:
        return HttpResponseRedirect(reverse('etudiants'))
    form = EtudiantForm(request.POST or None, request.FILES or None, instance=etudiant)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('etudiants'))
    return render(request, 'app/etudiants.html', {'form': form, 'etudiants': Etudiant.objects.all()})

# UEs
def ues(request):
    form = UEForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('ues'))
    ues = Ue.objects.all()
    return render(request, 'app/ues.html', {'form': form, 'ues': ues})

def supprimer_ue(request, id):
    try:
        Ue.objects.get(id_ue=id).delete()
    except Ue.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('ues'))

def modifier_ue(request, id):
    try:
        ue = Ue.objects.get(id_ue=id)
    except Ue.DoesNotExist:
        return HttpResponseRedirect(reverse('ues'))
    form = UEForm(request.POST or None, instance=ue)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('ues'))
    return render(request, 'app/ues.html', {'form': form, 'ues': Ue.objects.all()})

# Ressources
def ressources(request):
    form = RessourceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('ressources'))
    ressources = Ressource.objects.all()
    return render(request, 'app/ressources.html', {'form': form, 'ressources': ressources})

def supprimer_ressource(request, id):
    try:
        Ressource.objects.get(id_ressource=id).delete()
    except Ressource.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('ressources'))

def modifier_ressource(request, id):
    try:
        ressource = Ressource.objects.get(id_ressource=id)
    except Ressource.DoesNotExist:
        return HttpResponseRedirect(reverse('ressources'))
    form = RessourceForm(request.POST or None, instance=ressource)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('ressources'))
    return render(request, 'app/ressources.html', {'form': form, 'ressources': Ressource.objects.all()})

# Examens
def examens(request):
    form = ExamenForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('examens'))
    examens = Examen.objects.all()
    return render(request, 'app/examens.html', {'form': form, 'examens': examens})

def supprimer_examen(request, id):
    try:
        Examen.objects.get(id_examen=id).delete()
    except Examen.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('examens'))

def modifier_examen(request, id):
    try:
        examen = Examen.objects.get(id_examen=id)
    except Examen.DoesNotExist:
        return HttpResponseRedirect(reverse('examens'))
    form = ExamenForm(request.POST or None, instance=examen)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('examens'))
    return render(request, 'app/examens.html', {'form': form, 'examens': Examen.objects.all()})

# Notes
def notes(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('notes'))
    notes = Note.objects.all()
    return render(request, 'app/notes.html', {'form': form, 'notes': notes})

def supprimer_note(request, id):
    try:
        Note.objects.get(id_note=id).delete()
    except Note.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('notes'))

def modifier_note(request, id):
    try:
        note = Note.objects.get(id_note=id)
    except Note.DoesNotExist:
        return HttpResponseRedirect(reverse('notes'))
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('notes'))
    return render(request, 'app/notes.html', {'form': form, 'notes': Note.objects.all()})

# Import Notes
def import_notes(request):
    if request.method == "POST" and request.FILES.get("file"):
        csv_file = request.FILES["file"]
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            try:
                etudiant, _ = Etudiant.objects.get_or_create(
                    id_etudiant=row["etudiant_id"],
                    defaults={
                        "prenom": row["etudiant_prenom"],
                        "nom": row["etudiant_nom"],
                        "email": f"{row['etudiant_prenom'].lower()}.{row['etudiant_nom'].lower()}@etu.com",
                        "groupe": "A",

                    }
                )

                ue, _ = Ue.objects.get_or_create(
                    nom=row["ue_code"],
                    defaults={"semestre": 1, "credits": 6}
                )

                ressource, _ = Ressource.objects.get_or_create(
                    nom=row["ressource"],
                    ue=ue,
                    defaults={"description": f"SAE {row['ressource']}"}
                )

                examen, _ = Examen.objects.get_or_create(
                    id_examen=row["examen_id"],
                    defaults={"nom": row["examen_titre"], "date": "2025-01-01", "coefficient": 1.0, "id_ressource": ressource}
                )

                Note.objects.update_or_create(
                    id_etudiant=etudiant,
                    id_examen=examen,
                    defaults={"note": row["note"], "appreciation": row["appreciation"]}
                )
            except Exception as e:
                messages.error(request, f" Erreur ligne CSV : {e}")

        messages.success(request, " Importation terminée avec succès.")
        return redirect(reverse("import_notes"))

    return render(request, "app/import_notes.html", {"form": ImportCSVForm()})


# Enseignants
def enseignants(request):
    form = EnseignantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('enseignants'))
    enseignants = Enseignant.objects.all()
    return render(request, 'app/enseignants.html', {'form': form, 'enseignants': enseignants})

def supprimer_enseignant(request, id):
    try:
        Enseignant.objects.get(id_enseignant=id).delete()
    except Enseignant.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('enseignants'))

def modifier_enseignant(request, id):
    try:
        enseignant = Enseignant.objects.get(id_enseignant=id)
    except Enseignant.DoesNotExist:
        return HttpResponseRedirect(reverse('enseignants'))
    form = EnseignantForm(request.POST or None, instance=enseignant)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('enseignants'))
    return render(request, 'app/enseignants.html', {'form': form, 'enseignants': Enseignant.objects.all()})


def afficher_releve_html(request, id):
    etudiant = get_object_or_404(Etudiant, id_etudiant=id)

    ues_avec_moyennes = []
    for ue in Ue.objects.all():
        notes = Note.objects.filter(
            id_etudiant=etudiant,
            id_examen__id_ressource__ue=ue
        )
        if notes.exists():
            total_coef = sum(note.id_examen.coefficient for note in notes)
            total_pond = sum(note.note * note.id_examen.coefficient for note in notes)
            moyenne = total_pond / total_coef if total_coef > 0 else 0
        else:
            moyenne = 0

        # Récupérer les détails des notes pour cette UE
        lignes = []
        for note in notes:
            lignes.append({
                'ressource': note.id_examen.id_ressource.nom,
                'examen': note.id_examen.nom,
                'note': note.note,
                'coefficient': note.id_examen.coefficient,
                'appreciation': note.appreciation,
            })

        ues_avec_moyennes.append({'ue': ue, 'moyenne': moyenne, 'lignes': lignes})

    context = {
        'etudiant': etudiant,
        'ues_avec_moyennes': ues_avec_moyennes,
    }
    return render(request, 'app/releve_etudiant.html', context)
