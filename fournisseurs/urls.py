from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('liste', views.ListeFournisseurs.as_view(), name='fournisseurs-liste'),
    path('<slug:slug>/', views.DetailFournisseur.as_view(), name='fournisseur-detail'),
    path('update/<slug:slug>/', views.ModifierFournisseur.as_view(), name='fournisseur-modifier'),
]
