from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('liste', views.ListeFournisseurs.as_view(), name='fournisseurs-liste'),
]
