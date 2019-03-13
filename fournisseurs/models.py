from django.db import models

# Create your models here.
class Fournisseur(models.Model):
    TVA_CHOICES = (
        ('FR', 'France'),
        ('UE', 'Union Européenne'),
        ('IN', 'Import')
    )

    name = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    pays = models.CharField(max_length=100)
    tva = models.CharField(max_length=2, choices=TVA_CHOICES, default='France')
    contact = models.CharField(max_length=100)
    mail_contact = models.EmailField()
