from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Berita, Agenda, Dokumen
from django.db.models import Q

# Menampilkan daftar berita yang sudah diterbitkan
def daftar_berita(request):
    berita = Berita.objects.terbit().order_by('-tanggal_terbit')

    paginator = Paginator(berita, 6)
    halaman = paginator.get_page(request.GET.get('page'))

    return render(request, 'publikasi/daftar_berita.html', {
        'halaman': halaman,
    })


# Menampilkan detail berita
def detail_berita(request, slug):
    berita = get_object_or_404(
    Berita.objects.terbit(),
    slug=slug)

    return render(request, 'publikasi/detail_berita.html', {
        'berita': berita,
    })

# Menampilkan agenda kegiatan yang akan datang dan yang sudah lewat
def daftar_agenda(request):
    sekarang = timezone.now()

    agenda_mendatang = Agenda.objects.filter(
        waktu_mulai__gte=sekarang
    ).order_by('waktu_mulai')

    agenda_lampau = Agenda.objects.filter(
        waktu_mulai__lt=sekarang
    ).order_by('-waktu_mulai')

    agenda_rutin = Agenda.objects.filter(
        waktu_mulai__isnull=True
    )

    return render(request, 'publikasi/agenda.html', {
        'agenda_mendatang': agenda_mendatang,
        'agenda_lampau': agenda_lampau,
        'agenda_rutin': agenda_rutin,
    })

# Menampilkan daftar dokumen yang dapat diunduh
def daftar_dokumen(request):
    dokumen = Dokumen.objects.all()

    return render(request, 'publikasi/unduhan.html', {
        'daftar_dokumen': dokumen,
    })
