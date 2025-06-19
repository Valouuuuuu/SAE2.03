from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('etudiants/', views.etudiants, name='etudiants'),
    path('etudiants/supprimer/<int:id>/', views.supprimer_etudiant, name='supprimer_etudiant'),
    path('etudiants/modifier/<int:id>/', views.modifier_etudiant, name='modifier_etudiant'),

    path('ues/', views.ues, name='ues'),
    path('ues/supprimer/<int:id>/', views.supprimer_ue, name='supprimer_ue'),
    path('ues/modifier/<int:id>/', views.modifier_ue, name='modifier_ue'),

    path('ressources/', views.ressources, name='ressources'),
    path('ressources/supprimer/<int:id>/', views.supprimer_ressource, name='supprimer_ressource'),
    path('ressources/modifier/<int:id>/', views.modifier_ressource, name='modifier_ressource'),

    path('examens/', views.examens, name='examens'),
    path('examens/supprimer/<int:id>/', views.supprimer_examen, name='supprimer_examen'),
    path('examens/modifier/<int:id>/', views.modifier_examen, name='modifier_examen'),

    path('notes/', views.notes, name='notes'),
    path('notes/supprimer/<int:id>/', views.supprimer_note, name='supprimer_note'),
    path('notes/modifier/<int:id>/', views.modifier_note, name='modifier_note'),

    path("import-notes/", views.import_notes, name="import_notes"),

    path('enseignants/', views.enseignants, name='enseignants'),
    path('enseignants/supprimer/<int:id>/', views.supprimer_enseignant, name='supprimer_enseignant'),
    path('enseignants/modifier/<int:id>/', views.modifier_enseignant, name='modifier_enseignant'),
    path('releve/etudiant/<int:id>/', views.afficher_releve_html, name='releve_html'),

]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
