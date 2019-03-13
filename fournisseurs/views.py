from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView

from .models import Fournisseur

class ListeFournisseurs(ListView):
    model = Fournisseur

class DetailFournisseur(DetailView):
    model = Fournisseur

class ModifierFournisseur(UpdateView):
    model = Fournisseur
    fields = ['nom', 'adresse', 'code_postal', 'pays', 'tva', 'contact', 'mail_contact']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('fournisseurs-liste')

class CreerFournisseur(CreateView):
    model = Fournisseur
    fields = ['nom', 'adresse', 'code_postal', 'pays', 'tva', 'contact', 'mail_contact']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('fournisseurs-liste')
