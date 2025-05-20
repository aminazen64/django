from django import forms
from .models import (
    TbChantierSylviculture, 
    TbTravauxChantier, 
    TbEtat,
)

# ==== FORMULAIRE TRAVAUX ====
class TbTravauxChantierForm(forms.ModelForm):
    # Formulaire pour les travaux de chantier
    # (Le champ à définir sera fait dans la vue ou via l'URL)
    class Meta:
        model = TbTravauxChantier
        exclude = ['id_cs'] 
        fields = '__all__'
        
        # Ou spécifie explicitement les champs dont tu as besoin

class TbChantierSylvicultureForm(forms.ModelForm):
    class Meta:
        model = TbChantierSylviculture
        fields = '__all__'
        widgets = {
            'type_chantier': forms.Select(attrs={'id': 'id_type_chantier'}),
            'bureau': forms.Select(attrs={'id': 'id_bureau'}),
            'agence': forms.Select(attrs={'id': 'id_agence'}),
            'nom_propietaire': forms.TextInput(attrs={'id': 'id_nom_propietaire'}),
            'secteur': forms.Select(attrs={'id': 'id_secteur'}),
            'surface': forms.NumberInput(attrs={'id': 'id_surface'}),
            'subvention': forms.TextInput(attrs={'id': 'id_etat_garantie'}),
            'id_insee': forms.Select(attrs={'id': 'id_insee_commune'}),
        }
