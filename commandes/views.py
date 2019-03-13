from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView

from .models import Commande

class ListeCommandes(ListView):
    model = Commande

class DetailCommande(DetailView):
    model = Commande

class ModifierCommande(UpdateView):
    model = Commande
    fields = ['date_livraison', 'echeance', 'montant_ht', 'commande_livree']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('commandes-liste')

class CreerCommande(CreateView):
    model = Commande
    fields = ['fournisseur', 'saison', 'type_commande', 'référence', 'date_livraison', 'echeance', 'montant_ht']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('commandes-liste')
