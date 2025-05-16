from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/', views.ajouter_chantier, name='ajouter_chantier'),
   path('ajax/get-niv4/', views.get_niv4_by_niv3, name='get_niv4_by_niv3'),
    path('ajax/get-niv5/', views.get_niv5_by_niv4, name='get_niv5_by_niv4'),
    path('ajax/get-ops/', views.get_ops_by_niv5, name='get_ops_by_niv5'),
]
