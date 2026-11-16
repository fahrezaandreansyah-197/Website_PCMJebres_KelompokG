from django.contrib import admin
from .models import Berita, Agenda, Dokumen


# Pengaturan tampilan berita di Django Admin
@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal_terbit', 'status')
    search_fields = ('judul', 'ringkasan', 'isi')
    list_filter = ('status', 'tanggal_terbit')
    prepopulated_fields = {'slug': ('judul',)}
    date_hierarchy = 'tanggal_terbit'


# Pengaturan tampilan agenda
@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('nama_kegiatan', 'waktu_mulai', 'tempat')
    search_fields = ('nama_kegiatan', 'tempat')
    list_filter = ('waktu_mulai',)


# Pengaturan tampilan dokumen
@admin.register(Dokumen)
class DokumenAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal_unggah')
    search_fields = ('judul', 'keterangan')
    date_hierarchy = 'tanggal_unggah'
