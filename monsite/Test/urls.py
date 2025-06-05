from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/', views.ajouter_chantier, name='ajouter_chantier'),
    path('', lambda request: redirect('ajouter/')), 
    path('ajax/get-niv4/', views.get_niv4_by_niv3, name='get_niv4_by_niv3'),
    path('ajax/get-niv5/', views.get_niv5_by_niv4, name='get_niv5_by_niv4'),
    path('ajax/get-ops/', views.get_ops_by_niv5, name='get_ops_by_niv5'),
    path('get-chantier-details/', views.get_chantier_details, name='get_chantier_details'),
    path('chantiers/', views.liste_chantiers, name='liste_chantiers'),
    path('travaux/ajouter/<int:chantier_id>/', views.ajouter_travaux_chantier, name='ajouter_travaux_chantier'),
    path('chantiers/<int:id>/voir-travaux/', views.voir_travaux_chantier, name='voir_travaux_chantier'),
    #path('ajouter-plante/', views.ajouter_plant_souhaite, name='ajouter_plante'),
    path('ajax/get_provenances/', views.get_provenances_by_essence, name='get_provenances_by_essence'),
    path('ajax/get_agedetaille/', views.get_agedetaille_by_agesimple, name='get_agedetaille_by_agesimple'),
    path('ajax/get_cond_precis/', views.get_cond_precis_by_cond, name='get_cond_precis_by_cond'),
    path('plants/', views.liste_plants, name='liste_plants'),
    path('ilot/<int:ilot_id>/plants/<int:ps_id>/ajouter-soin/', views.ajouter_soin_pour_plant, name='ajouter_soin_plant'),
    path('ilot/<int:ilot_id>/plants/<int:ps_id>/reguler/', views.reguler_plant, name='reguler_plant'),
    path('plants/<int:ps_id>/reguls/', views.voir_regul, name='voir_regul'),
    path('get-niv4-by-niv3/', views.get_niv4_by_niv3_soins, name='get_niv4_by_niv3_soins'),
    path('get-niv5-by-niv4/', views.get_niv5_by_niv4_soins, name='get_niv5_by_niv4_soins'),
    path('get-ops-by-niv5/', views.get_ops_by_niv5_soins, name='get_ops_by_niv5_soins'),
    path('plants/<int:plant_id>/soins/', views.liste_soins_plants, name='liste_soins_plants'),
    path('ilots/<int:chantier_id>/', views.liste_ilots_chantiers, name='liste_ilots'),
    path('ilot/<int:ilot_id>/plants/ajouter/', views.ajouter_plant_souhaite, name='ajouter_plante'),
    path('ilot/<int:ilot_id>/plants/', views.liste_plants, name='liste_plants_pour_ilot'),
]


