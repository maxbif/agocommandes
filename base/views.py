from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class Accueil(TemplateView):

    template_name = "base\home.html"
