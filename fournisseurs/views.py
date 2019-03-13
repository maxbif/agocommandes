from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Fournisseur

class ListeFournisseurs(ListView):
    model = Fournisseur
