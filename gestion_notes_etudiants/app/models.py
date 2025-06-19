from django.db import models


class Enseignant(models.Model):
    id_enseignant = models.AutoField(db_column='ID_Enseignant', primary_key=True)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=255)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        managed = False
        db_table = 'enseignant'


class Etudiant(models.Model):
    id_etudiant = models.AutoField(db_column='ID_Etudiant', primary_key=True)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=255)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255)  # Field name made lowercase.
    groupe = models.CharField(db_column='Groupe', max_length=20)  # Field name made lowercase.


    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        managed = False
        db_table = 'etudiant'


class Examen(models.Model):
    id_examen = models.AutoField(db_column='ID_Examen', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient')  # Field name made lowercase.
    id_ressource = models.ForeignKey('Ressource', models.DO_NOTHING, db_column='ID_Ressource')  # Field name made lowercase.
    id_enseignant = models.ForeignKey(Enseignant, models.DO_NOTHING, db_column='ID_Enseignant', blank=True, null=True)  # Field name made lowercase.


    def __str__(self):
        return self.nom

    class Meta:
        managed = False
        db_table = 'examen'


class Note(models.Model):
    id_note = models.AutoField(db_column='ID_Note', primary_key=True)  # Field name made lowercase.
    note = models.FloatField(db_column='Note')  # Field name made lowercase.
    appreciation = models.TextField(db_column='Appreciation')  # Field name made lowercase.
    id_etudiant = models.ForeignKey(Etudiant, models.DO_NOTHING, db_column='ID_Etudiant')  # Field name made lowercase.
    id_examen = models.ForeignKey(Examen, models.DO_NOTHING, db_column='ID_Examen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'note'
        unique_together = (('id_etudiant', 'id_examen'),)


class Ressource(models.Model):
    id_ressource = models.AutoField(db_column='ID_Ressource', primary_key=True)  # Field name made lowercase.
    ue = models.ForeignKey('Ue', models.DO_NOTHING, db_column='UE_ID')  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.

    def __str__(self):
        return self.nom

    class Meta:
        managed = False
        db_table = 'ressource'


class Ue(models.Model):
    id_ue = models.AutoField(db_column='ID_UE', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255)  # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre')  # Field name made lowercase.
    credits = models.IntegerField(db_column='Credits')  # Field name made lowercase.

    def __str__(self):
        return self.nom

    class Meta:
        managed = False
        db_table = 'ue'
        unique_together = (('nom', 'semestre'),)