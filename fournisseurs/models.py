from django.db import models
from django.template.defaultfilters import slugify

from django_countries.fields import CountryField

from datetime import datetime

# Create your models here.
class Fournisseur(models.Model):
    TVA_CHOICES = (
        ('FR', 'France'),
        ('UE', 'Union Européenne'),
        ('IN', 'Import')
    )

    nom = models.CharField(max_length=100)
    adresse = models.TextField(max_length=100)
    code_postal = models.CharField(max_length=10)
    pays = CountryField(blank_label='(select country)')
    tva = models.CharField(max_length=10, choices=TVA_CHOICES)
    taux_tva = models.DecimalField(max_digits=4, decimal_places=2)
    contact = models.CharField(max_length=100, blank=True)
    mail_contact = models.EmailField()
    date_created= models.DateTimeField(default=datetime.now)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if self.tva == 'FR' or self.tva == 'UE':
            self.taux_tva = 20.00
        else :
            self.taux_tva = 0
        self.slug = slugify(self.nom)
        super(Fournisseur, self).save(*args, **kwargs)
