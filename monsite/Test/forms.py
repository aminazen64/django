from django import forms
from .models import (
    TbChantierSylviculture, TbTravauxChantier, TbEtat,
    VSociete, VBureau, VCommune, VPepiniere,
    V_TYPEChantier, VNiv3TRAV, VNiV4TRAV, VNIV5TRAV,
    VTypeOperation, VSousTraitant
)

# ==== FORMULAIRE TRAVAUX ====

class TbTravauxChantierForm(forms.ModelForm):
    travaux_niv3_n = forms.ModelChoiceField(
        queryset=VNiv3TRAV.objects.all(),
        label="Travaux Niveau 3"
    )

    travaux_niv4_n = forms.ModelChoiceField(
        queryset=VNiV4TRAV.objects.all(),
        required=False,
        label="Travaux Niveau 4"
    )

    travaux_niv5_n = forms.ModelChoiceField(
        queryset=VNIV5TRAV.objects.all(),
        required=False,
        label="Travaux Niveau 5"
    )

    type_operation_n = forms.ModelChoiceField(
        queryset=VTypeOperation.objects.all(),
        required=False,
        label="Type Opération"
    )

    sous_traitant_n = forms.ModelChoiceField(
        queryset=VSousTraitant.objects.all(),
        label="Sous-traitant"
    )

    class Meta:
        model = TbTravauxChantier
        exclude = ['id_cs']  # car il sera défini dans la vue ou via l'URL

# ==== FORMULAIRE CHANTIER ====

class TbChantierSylvicultureForm(forms.ModelForm):
    societe_n = forms.ModelChoiceField(
        queryset=VSociete.objects.all(),
        label="Société"
    )

    bureau_n = forms.ModelChoiceField(
        queryset=VBureau.objects.all(),
        label="Bureau"
    )

    commune_n = forms.ModelChoiceField(
        queryset=VCommune.objects.all(),
        label="Commune"
    )

    pepiniere_n = forms.ModelChoiceField(
        queryset=VPepiniere.objects.all(),
        label="Pépinière"
    )

    type_chantier_n = forms.ModelChoiceField(
        queryset=V_TYPEChantier.objects.all(),
        label="Type de Chantier"
    )

    id_etat_n = forms.ModelChoiceField(
        queryset=TbEtat.objects.all(),
        label="État"
    )

    class Meta:
        model = TbChantierSylviculture
        fields = [
            'societe_n',
            'type_chantier_n',
            'proprietaire_n',
            'proprietaire_libelle_libre_a',
            'bureau_n',
            'secteur_n',
            'important',
            'surface_indicative_reboisement_n',
            'commune_n',
            'pepiniere_n',
            'id_etat_n',
        ]
