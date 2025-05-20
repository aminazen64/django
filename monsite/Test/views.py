from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import TbChantierSylvicultureForm, TbTravauxChantierForm
from .models import TbChantierSylviculture, VNiV4TRAV, VNIV5TRAV, VTypeOperation, VNiv3TRAV, VChantier


def get_chantier_details(request):
    code_chantier = request.GET.get('code_chantier')
    if not code_chantier:
        return JsonResponse({'error': 'Code chantier manquant'}, status=400)

    try:
        chantier = VChantier.objects.get(code_chantier=code_chantier.strip())
        return JsonResponse({
            'agence': chantier.agence,
            'bureau': chantier.bureau,
            'propietaire': chantier.proprietaire,
            'secteur': chantier.secteur,
            'surface': chantier.surface,
            'etat_garantie': chantier.etat_garantie,
            'insee_commune': chantier.insee_commune,
        })
    except VChantier.DoesNotExist:
        return JsonResponse({'error': 'Chantier non trouvé'}, status=404)


def get_niv4_by_niv3(request):
    niv3_id = request.GET.get('niv3_id')
    niv4_options = VNiV4TRAV.objects.filter(nv4_codnv3_n=niv3_id).values('nv4_codnv4_n', 'nv4_lib_a')
    return JsonResponse(list(niv4_options), safe=False)


def get_niv5_by_niv4(request):
    niv4_id = request.GET.get('niv4_id')
    niv5_options = VNIV5TRAV.objects.filter(nv5_codnv4_n=niv4_id).values('nv5_codnv5_n', 'nv5_lib_a')
    return JsonResponse(list(niv5_options), safe=False)


def get_ops_by_niv5(request):
    niv5_id = request.GET.get('niv5_id')
    op_options = VTypeOperation.objects.filter(typ_codnv5_n=niv5_id).values('typ_codope_n', 'typ_libope_a')
    return JsonResponse(list(op_options), safe=False)


def ajouter_chantier(request):
    if request.method == 'POST':
        chantier_form = TbChantierSylvicultureForm(request.POST)
        travaux_form = TbTravauxChantierForm(request.POST)

        if chantier_form.is_valid() and travaux_form.is_valid():
            chantier = chantier_form.save()
            travaux = travaux_form.save(commit=False)
            travaux.id_cs = chantier
            travaux.save()
            return redirect('liste_chantiers')
        else:
            # Si les formulaires ne sont pas valides, afficher les erreurs
            print(chantier_form.errors)
            print(travaux_form.errors)
    else:
        chantier_form = TbChantierSylvicultureForm()
        travaux_form = TbTravauxChantierForm()

    context = {
        'chantier_form': chantier_form,
        'travaux_form': travaux_form
    }
    return render(request, 'ajouter_reb.html', context)

def liste_chantiers(request):
    chantiers = TbChantierSylviculture.objects.all().select_related(
        'id_insee', 'societe', 'type_chantier'
    )

    return render(request, 'list_reb.html', {
        'chantiers': chantiers
    })