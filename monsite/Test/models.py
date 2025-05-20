# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class VBureau(models.Model):
    code_bureau = models.IntegerField(primary_key=True)
    nom_bureau = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'V_BUREAUX'
    def __str__(self):
        return self.nom_bureau

class VCommune(models.Model):
    id_commune_n = models.CharField(max_length=100,primary_key=True)
    communespesi = models.CharField(max_length=100)

    def __str__(self):
        return self.communespesi

    class Meta:
        managed = False
        db_table = 'V_COMMUNES'


class VPepiniere(models.Model):
    code_pepiniere = models.CharField(max_length=20, primary_key=True)
    nom_pepiniere = models.CharField(max_length=150)

    def __str__(self):
        return self.nom_pepiniere

    class Meta:
        managed = False
        db_table = 'V_PEPINIERES'


class VSociete(models.Model):
    soc_code_n = models.IntegerField(primary_key=True)
    societe = models.CharField(max_length=100)

    def __str__(self):
        return self.societe

    class Meta:
        managed = False
        db_table = 'V_SOCIETES'


class V_TYPEChantier(models.Model):
    code_chantier = models.CharField(max_length=50, primary_key=True)
    chantier_detail = models.CharField(max_length=255)

    def __str__(self):
        return self.chantier_detail

    class Meta:
        managed = False
        db_table = 'V_CHANTIER' 


class VNiv3TRAV(models.Model):
    nv3_codnv3_n = models.IntegerField(primary_key=True)
    nv3_lib_a = models.CharField(max_length=100)

    def __str__(self):
        return self.nv3_lib_a

    class Meta:
        managed = False
        db_table = 'V_NIV3_TRAVAUX'  


class VNiV4TRAV(models.Model):
    nv4_codnv4_n = models.IntegerField(primary_key=True)
    nv4_lib_a = models.CharField(max_length=100)
    nv4_codnv3_n = models.ForeignKey(
        VNiv3TRAV,
        on_delete=models.DO_NOTHING,
        db_column='nv4_codnv3_n'
    )

    def __str__(self):
        return self.nv4_lib_a

    class Meta:
        managed = True
        db_table = 'V_NIV4_TRAVAUX'



class VNIV5TRAV(models.Model):
    nv5_codnv5_n = models.IntegerField(primary_key=True)
    nv5_lib_a = models.CharField(max_length=100)
    nv5_codnv4_n = models.ForeignKey(
        VNiV4TRAV,
        on_delete=models.DO_NOTHING,
        db_column='nv5_codnv4_n'
    )

    def __str__(self):
        return self.nv5_lib_a

    class Meta:
        managed = True
        db_table = 'V_NIV5_TRAVAUX'



class VTypeOperation(models.Model):
    typ_codope_n = models.IntegerField(primary_key=True)
    typ_libope_a = models.CharField(max_length=100)
    typ_codnv5_n = models.ForeignKey(
        VNIV5TRAV,
        on_delete=models.DO_NOTHING,
        db_column='typ_codnv5_n'
    )

    def __str__(self):
        return self.typ_libope_a

    class Meta:
        managed = True
        db_table = 'V_TYPEOPE_TRAVAUX'
        

class VSousTraitant(models.Model):
    code_statut = models.CharField(max_length=20, primary_key=True)
    sous_traitants = models.CharField(max_length=255)

    def __str__(self):
        return self.sous_traitants

    class Meta:
        managed = False
        db_table = 'V_SOUS_TRAITANTS'

class VChantier(models.Model):
    code_chantier = models.ForeignKey(V_TYPEChantier, on_delete=models.CASCADE, db_column='code_chantier', primary_key=True)
    etat_garantie = models.CharField(max_length=10, blank=True, null=True)
    agence = models.CharField(max_length=50, blank=True, null=True)
    bureau = models.CharField(max_length=50, blank=True, null=True)
    secteur = models.CharField(max_length=50, blank=True, null=True)
    surface = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    insee_commune = models.CharField(max_length=10, blank=True, null=True)
    proprietaire = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False  
        db_table = 'v_CHANTIERS_RECUPERATION_DATA'
         
class VSecteur(models.Model):
 
    code_secteur = models.CharField(max_length=10, primary_key=True)  # Clé primaire
    libelle_secteur = models.CharField(max_length=255)  # Libellé du secteur
    code_agence = models.CharField(max_length=10)  

    def __str__(self):
        return self.libelle_secteur

    class Meta:
        managed = False  
        db_table = 'V_SECTEURS'
        
class VAgence(models.Model):
    agence = models.CharField(max_length=10, primary_key=True)  # Clé primaire pour l'agence

    def __str__(self):
        return self.agence

    class Meta:
        managed = False  # Ce modèle représente une vue, donc pas de migrations
        db_table = 'V_AGENCES'  

class ChantierSylvicultureHistory(models.Model):
    idchantier_sylviculture = models.IntegerField(db_column='IDchantier_sylviculture')  # Field name made lowercase.
    societe = models.CharField(max_length=50, db_collation='French_CI_AS', blank=True, null=True)
    secteur = models.CharField(max_length=50, db_collation='French_CI_AS', blank=True, null=True)
    bureau = models.CharField(max_length=50, db_collation='French_CI_AS', blank=True, null=True)
    type_chantier = models.CharField(max_length=50, db_collation='French_CI_AS')
    commune = models.CharField(max_length=50, db_collation='French_CI_AS')
    surface_r = models.CharField(db_column='surface_R', max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    pepiniere = models.CharField(max_length=50, db_collation='French_CI_AS')
    subvention = models.CharField(max_length=50, db_collation='French_CI_AS')
    entreprise_prep = models.CharField(max_length=50, db_collation='French_CI_AS')
    planteur = models.CharField(max_length=50, db_collation='French_CI_AS')
    blocknote = models.CharField(max_length=50, db_collation='French_CI_AS')
    date_creation = models.DateTimeField()
    validfrom = models.DateTimeField(db_column='ValidFrom')  # Field name made lowercase.
    validto = models.DateTimeField(db_column='ValidTo')  # Field name made lowercase.
    client = models.CharField(max_length=40, db_collation='French_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Chantier_sylviculture_History'


class TbChantierSylviculture(models.Model):
    id_chantier_sylviculture_n = models.AutoField(db_column='Id_Chantier_Sylviculture_n', primary_key=True)  # Field name made lowercase.
    important = models.BooleanField(blank=True, null=True)
    surface = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    proprietaire_libelle_libre = models.CharField(max_length=50, db_collation='French_CI_AS', blank=True, null=True)
    subvention = models.CharField(max_length=1, db_collation='French_CI_AS', blank=True, null=True)
    bloc_note = models.CharField(max_length=50, db_collation='French_CI_AS', blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    societe =models.ForeignKey(VSociete, on_delete=models.CASCADE, blank=True, null=True ,db_column="societe")
    agence = models.ForeignKey(VAgence, on_delete=models.CASCADE, blank=True, null=True , db_column="agence")
    bureau = models.ForeignKey(VBureau, on_delete=models.CASCADE, blank=True, null=True , db_column="bureau")
    secteur = models.ForeignKey(VSecteur, on_delete=models.CASCADE, blank=True, null=True , db_column="secteur")
    type_chantier = models.ForeignKey(V_TYPEChantier , on_delete= models.CASCADE , db_column="type_chantier")  # Field name made lowercase.
    id_insee = models.ForeignKey(VCommune, models.DO_NOTHING, db_column='id_insee', blank=True, null=True)
    id_pepiniere = models.ForeignKey(VPepiniere, models.DO_NOTHING, db_column='id_pepiniere', blank=True, null=True)
    nom_propietaire = models.CharField(max_length=50, db_collation='French_CI_AS', blank=True, null=True)
    etat_id_n = models.ForeignKey('TbEtat', models.DO_NOTHING, db_column='etat_id_n', blank=True, null=True)
    u_id_n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_Chantier_sylviculture'


class TbEtat(models.Model):
    id_etat_n = models.AutoField(db_column='Id_etat_n', primary_key=True)  # Field name made lowercase.
    type_a = models.CharField(max_length=50, db_collation='French_CI_AS', blank=True, null=True)
    ordre_n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_Etat'
    def __str__(self):
        return self.type_a


class TbTest(models.Model):
    id = models.OneToOneField('self', models.DO_NOTHING, db_column='id', primary_key=True)
    tes_testi_a = models.CharField(max_length=50, db_collation='French_CI_AS', blank=True, null=True)
    id_societe = models.CharField(max_length=10, db_collation='French_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_TEST'


class TbTest3(models.Model):
    ta_id_n = models.AutoField(primary_key=True)
    ta_libelle_a = models.CharField(max_length=50, db_collation='French_CI_AS', blank=True, null=True)
    e_id_n = models.IntegerField(blank=True, null=True)
    ordre_n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_Test3'


class TbTravauxChantier(models.Model):
    id_travaux_n = models.AutoField(primary_key=True)
    annee_n = models.IntegerField(blank=True, null=True)
    numero_semaine_a = models.CharField(max_length=1, db_collation='French_CI_AS', blank=True, null=True)
    quantite_n = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    travaux_niv3_n = models.ForeignKey(VNiv3TRAV, models.DO_NOTHING, db_column='travaux_niv3_n', blank=True, null=True)
    travaux_niv4_n = models.ForeignKey(VNiV4TRAV, models.DO_NOTHING, db_column='travaux_niv4_n', blank=True, null=True)
    travaux_niv5_n = models.ForeignKey(VNIV5TRAV, models.DO_NOTHING, db_column='travaux_niv5_n', blank=True, null=True)
    type_operation_n = models.ForeignKey(VTypeOperation, models.DO_NOTHING, db_column='type_operation_n', blank=True, null=True)
    sous_traitant_n = models.ForeignKey(VSousTraitant, models.DO_NOTHING, db_column='sous_traitant_n', blank=True, null=True)
    id_cs = models.ForeignKey(TbChantierSylviculture, models.DO_NOTHING, db_column='id_cs')

    class Meta:
        managed = False
        db_table = 'TB_Travaux_chantier'


class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(db_column='Id_utilisateur', primary_key=True)  # Field name made lowercase.
    prenom = models.CharField(max_length=100, db_collation='French_CI_AS', blank=True, null=True)
    nom = models.CharField(max_length=100, db_collation='French_CI_AS', blank=True, null=True)
    email = models.CharField(max_length=100, db_collation='French_CI_AS', blank=True, null=True)
    motdepasse = models.CharField(max_length=100, db_collation='French_CI_AS', blank=True, null=True)
    role = models.CharField(max_length=50, db_collation='French_CI_AS', blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Utilisateur'


class Utilisateurprocofor(models.Model):
    username = models.CharField(max_length=50, db_collation='French_CI_AS')
    role = models.CharField(max_length=2, db_collation='French_CI_AS')
    id_utili_n = models.AutoField(primary_key=True)
    user_djan = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='user_djan', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UtilisateurProcofor'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='French_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='French_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='French_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='French_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='French_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='French_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='French_CI_AS')
    email = models.CharField(max_length=254, db_collation='French_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='French_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='French_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='French_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='French_CI_AS')
    model = models.CharField(max_length=100, db_collation='French_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='French_CI_AS')
    name = models.CharField(max_length=255, db_collation='French_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='French_CI_AS')
    session_data = models.TextField(db_collation='French_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
