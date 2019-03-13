from django.apps import AppConfig

from .models import Fournisseur

class FournisseursConfig(AppConfig):
    name = 'fournisseurs'

admin.site.register(Fournisseur)
