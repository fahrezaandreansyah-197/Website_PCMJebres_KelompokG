from django.contrib import admin
from .models import MajelisLembaga

from .models import (
    ProfilOrganisasi,
    Pimpinan,
    Ranting,
    AmalUsaha,
    TautanTerkait,
)

@admin.register(ProfilOrganisasi)
class ProfilOrganisasiAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nama_singkat', 'alamat')

    def has_add_permission(self, request):
        # Hanya boleh ada satu profil organisasi
        return not ProfilOrganisasi.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Profil organisasi tidak boleh dihapus
        return False


@admin.register(Pimpinan)
class PimpinanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jabatan', 'periode', 'urutan')
    search_fields = ('nama', 'jabatan')
    list_filter = ('periode',)


@admin.register(Ranting)
class RantingAdmin(admin.ModelAdmin):
    list_display = ('nama_ranting', 'ketua')
    search_fields = ('nama_ranting', 'ketua')


@admin.register(AmalUsaha)
class AmalUsahaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'bidang')
    search_fields = ('nama',)
    list_filter = ('bidang',)

@admin.register(TautanTerkait)
class TautanTerkaitAdmin(admin.ModelAdmin):
    list_display = ('nama', 'url', 'urutan')
    search_fields = ('nama',)
    ordering = ('urutan', 'nama')

@admin.register(MajelisLembaga)
class MajelisLembagaAdmin(admin.ModelAdmin):
    list_display = ('urutan', 'nama_jabatan', 'nama_ketua')
    list_display_links = ('nama_jabatan',)
    search_fields = ('nama_jabatan', 'nama_ketua')
    list_editable = ('urutan',)
    ordering = ('urutan',)