from .models import ProfilOrganisasi, TautanTerkait

def informasi_global(request):
    return {
        'profil_global': ProfilOrganisasi.objects.first(),
        'tautan_global': TautanTerkait.objects.all(),
    }
