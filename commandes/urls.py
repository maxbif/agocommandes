from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('encours/', views.ListeCommandesEnCours.as_view(), name='encours-liste'),
    path('livrees/', views.ListeCommandesLivrees.as_view(), name='livrees-liste'),
    path('create/', views.CreerCommande.as_view(), name='commande-creer'),
    path('<slug:slug>/', views.DetailCommande.as_view(), name='commande-detail'),
    path('update/<slug:slug>/', views.ModifierCommande.as_view(), name='commande-modifier'),
]
