from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .models import Fournisseur

class ListeFournisseurs(ListView):
    model = Fournisseur

class DetailFournisseur(DetailView):
    model = Fournisseur

class ModifierFournisseur(UpdateView):
    model = Fournisseur
    fields = ['name', 'adresse', 'contact']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('fournisseurs-liste')
