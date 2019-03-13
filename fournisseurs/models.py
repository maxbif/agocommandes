from django.db import models

from datetime import datetime

# Create your models here.
class Fournisseur(models.Model):
    TVA_CHOICES = (
        ('FR', 'France'),
        ('UE', 'Union Européenne'),
        ('IN', 'Import')
    )

    name = models.CharField(max_length=100)
    adresse = models.TextField(max_length=100)
    code_postal = models.CharField(max_length=10)
    pays = models.CharField(max_length=100)
    tva = models.CharField(max_length=2, choices=TVA_CHOICES, default='France')
    taux_tva = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    mail_contact = models.EmailField()
    date_created= models.DateTimeField(default=datetime.now)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
