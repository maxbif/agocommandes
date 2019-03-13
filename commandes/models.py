from django.db import models
from django.template.defaultfilters import slugify

from django_countries.fields import CountryField

from datetime import datetime

from fournisseurs.models import Fournisseur

class Commande(models.Model):
    TYPE_CHOICES = (
        ('IN', 'Initiale'),
        ('RE', 'Reassort'),
    )

    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    saison = models.CharField(max_length=4)
    type_commande = models.CharField(max_length=2, choices=TYPE_CHOICES)
    référence = models.CharField(max_length=100)
    date = models.DateField()
    echeance = models.DateField()
    montant_ht = models.DecimalField(max_digits=10, decimal_places=2)
    montant_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    date_created= models.DateTimeField(default=datetime.now)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug = slugify(string(self.fournisseur.nom)+string(self.saison)+string(self.type_commande)+string(self.référence)[:4])
        self.montant_ttc = self.montant_ht * (1 + self.fournisseur.taux_tva/100)
        super(Commande, self).save(*args, **kwargs)
