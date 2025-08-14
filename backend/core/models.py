from django.db import models

# Create your models here.
from django.db import models
import uuid

class Utilisateur(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    mot_de_passe_hash = models.CharField(max_length=255)
    email_confirme = models.BooleanField(default=False)
    dernière_connexion = models.DateTimeField(null=True, blank=True)
    tentatives_connexion = models.IntegerField(default=0)
    verrouillé_jusquà = models.DateTimeField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'utilisateurs'
        managed = False