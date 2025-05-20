$(document).ready(function () {
    // Activer Select2
    $('select').select2({ width: '100%' });

    // Niveau 3 → Niveau 4
    $('#id_travaux_niv3_n').on('change', function () {
        const niv3Id = $(this).val();
        if (!niv3Id) return;

        $.get(getNiv4Url, { niv3_id: niv3Id }, function (data) {
            $('#id_travaux_niv4_n').empty().append('<option value="">---------</option>');
            $('#id_travaux_niv5_n, #id_type_operation_n').empty().append('<option value="">---------</option>');

            data.forEach(function (item) {
                $('#id_travaux_niv4_n').append(new Option(item.nv4_lib_a, item.nv4_codnv4_n));
            });

            $('#id_travaux_niv4_n').trigger('change');
        });
    });

    // Niveau 4 → Niveau 5
    $('#id_travaux_niv4_n').on('change', function () {
        const niv4Id = $(this).val();
        if (!niv4Id) return;

        $.get(getNiv5Url, { niv4_id: niv4Id }, function (data) {
            $('#id_travaux_niv5_n').empty().append('<option value="">---------</option>');
            $('#id_type_operation_n').empty().append('<option value="">---------</option>');

            data.forEach(function (item) {
                $('#id_travaux_niv5_n').append(new Option(item.nv5_lib_a, item.nv5_codnv5_n));
            });

            $('#id_travaux_niv5_n').trigger('change');
        });
    });

    // Niveau 5 → Type opération
    $('#id_travaux_niv5_n').on('change', function () {
        const niv5Id = $(this).val();
        if (!niv5Id) return;

        $.get(getOpsUrl, { niv5_id: niv5Id }, function (data) {
            $('#id_type_operation_n').empty().append('<option value="">---------</option>');
            data.forEach(function (item) {
                $('#id_type_operation_n').append(new Option(item.typ_libope_a, item.typ_codope_n));
            });
        });
    });

    // Type de chantier → Remplir infos
    $('#id_type_chantier').on('change', function () {
        const codeChantier = $(this).val();
        if (!codeChantier) return;

        $.get(getChantierDetailsUrl, { code_chantier: codeChantier }, function (data) {
            console.log(data);
            if (data.error) {
                console.warn("Erreur:", data.error);
                return;
            }

            if ($('#id_bureau').length) {
                $('#id_bureau').val(data.bureau).trigger('change.select2').prop('disabled', true);
            }
            if ($('#id_agence').length) {
                $('#id_agence').val(data.agence).trigger('change.select2').prop('disabled', true);
            }
            if ($('#id_nom_propietaire').length) {
                $('#id_nom_propietaire').val(data.propietaire).prop('disabled', true);
            }
            if ($('#id_secteur').length) {
                $('#id_secteur').val(data.secteur).trigger('change.select2').prop('disabled', true);
            }
            if ($('#id_surface').length) {
                $('#id_surface').val(data.surface);
            }
            if ($('#id_etat_garantie').length) {
                $('#id_etat_garantie').val(data.etat_garantie).prop('disabled', true);
            }
            if ($('#id_insee_commune').length) {
                $('#id_insee_commune').val(data.insee_commune).trigger('change.select2').prop('readonly', true);
            }
        });
    });
});
