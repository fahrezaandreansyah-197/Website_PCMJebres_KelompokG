from django.contrib import admin
from .models import PesanMasuk

# Pengaturan tampilan pesan masuk
@admin.register(PesanMasuk)
class PesanMasukAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'subjek', 'waktu_kirim', 'sudah_dibaca')
    search_fields = ('nama', 'email', 'subjek')
    list_filter = ('sudah_dibaca', 'waktu_kirim')

    # Pesan pengunjung hanya dapat dibaca, tidak diedit
    readonly_fields = (
        'nama',
        'email',
        'subjek',
        'pesan',
        'waktu_kirim',
        'sudah_dibaca',
    )

    def has_add_permission(self, request):
        return False

    # Otomatis menandai pesan sudah dibaca ketika detail dibuka
    def change_view(self, request, object_id, form_url="", extra_context=None):
        pesan = self.get_object(request, object_id)

        if pesan and not pesan.sudah_dibaca:
            PesanMasuk.objects.filter(pk=pesan.pk).update(
                sudah_dibaca=True
            )

        return super().change_view(
            request, object_id, form_url, extra_context
        )
