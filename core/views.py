from django.shortcuts import render
from django.utils import timezone
from .models import ProfilOrganisasi, Pimpinan, Ranting, AmalUsaha, MajelisLembaga
from publikasi.models import Berita, Agenda
from django.db.models import Q

def home(request):
    # Mengambil profil organisasi
    profil = ProfilOrganisasi.objects.first()

    # Menghitung jumlah ranting dan amal usaha
    jumlah_ranting = Ranting.objects.count()
    jumlah_amal_usaha = AmalUsaha.objects.count()

    # Mengambil jumlah anggota KTAM jika datanya tersedia
    jumlah_ktam = None
    if profil and profil.jumlah_anggota_ktam > 0:
        jumlah_ktam = profil.jumlah_anggota_ktam

    # Mengambil maksimal 3 berita terbaru yang sudah diterbitkan
    berita_terbaru = Berita.objects.filter(
        status='terbit',
        tanggal_terbit__lte=timezone.now()
    ).order_by('-tanggal_terbit')[:3]

    # Mengambil maksimal 3 agenda yang akan datang
    agenda_mendatang = Agenda.objects.filter(
    Q(waktu_mulai__gte=timezone.now()) |
    Q(waktu_mulai__isnull=True)).order_by('waktu_mulai')[:3]

    context = {
        'profil': profil,
        'nama_pcm': 'Pimpinan Cabang Muhammadiyah Jebres',
        'alamat': 'Jln. Tentara Pelajar No. 1, Kandang Sapi, Jebres, Surakarta',
        'jumlah_ranting': jumlah_ranting,
        'jumlah_amal_usaha': jumlah_amal_usaha,
        'jumlah_ktam': jumlah_ktam,
        'berita_terbaru': berita_terbaru,
        'agenda_mendatang': agenda_mendatang,
    }

    return render(request, 'core/home.html', context)


def profil(request):
    data_profil = ProfilOrganisasi.objects.first()
    return render(request, 'core/profil.html', {'profil': data_profil})


def pimpinan(request):
    data_pimpinan = Pimpinan.objects.all()
    data_majelis = MajelisLembaga.objects.all()

    context = {
        'daftar_pimpinan': data_pimpinan,
        'daftar_majelis': data_majelis,
    }

    return render(request, 'core/pimpinan.html', context)


def ranting(request):
    data_ranting = Ranting.objects.all()
    return render(request, 'core/ranting.html', {'daftar_ranting': data_ranting})


def amal_usaha(request):
    data_amal = AmalUsaha.objects.all()
    return render(request, 'core/amal_usaha.html', {'daftar_amal': data_amal})
