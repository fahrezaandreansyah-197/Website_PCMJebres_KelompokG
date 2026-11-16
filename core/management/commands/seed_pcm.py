from django.core.management.base import BaseCommand
from core.models import ProfilOrganisasi, Pimpinan, AmalUsaha, TautanTerkait


class Command(BaseCommand):
    help = 'Mengisi data awal organisasi PCM Jebres'

    def handle(self, *args, **options):

        # Data profil organisasi
        ProfilOrganisasi.objects.update_or_create(
            pk=1,
            defaults={
                'nama': 'Pimpinan Cabang Muhammadiyah Jebres',
                'nama_singkat': 'PCM Jebres',
                'tagline': 'Mengembangkan dakwah Islamiyah yang berkemajuan',
                'tentang': (
                    'Pimpinan Cabang Muhammadiyah Jebres merupakan '
                    'organisasi Muhammadiyah yang berada di wilayah '
                    'Kecamatan Jebres, Kota Surakarta.'
                ),
                'sejarah': (
                    'PCM Jebres berdiri pada 18 April 1963 dengan nama '
                    'awal Muhammadiyah Grub Solo Timur.'
                ),
                'visi': (
                    'Mengembangkan dakwah Islamiyah yang berkemajuan, '
                    'sehingga menjadi Cabang unggulan yang bermanfaat '
                    'bagi Umat Islam khususnya dan masyarakat pada umumnya.'
                ),
                'misi': (
                    'Mengemban tugas dakwah Islamiyah di lingkungan '
                    'Jebres pada khususnya dan masyarakat luas pada umumnya.'
                ),
                'alamat': (
                    'Jln. Tentara Pelajar No. 1, Kandang Sapi, '
                    'Jebres, Surakarta.'
                ),
            }
        )

        # Data pimpinan periode 2022–2027
        daftar_pimpinan = [
            ('H. Bambang Condro Haryadi, S.Pd', 'Ketua'),
            ('Prof. Dr. H. Heri Sawiji, M.Pd.', 'Wakil Ketua'),
            ('Drs. Joko Hariyanto', 'Sekretaris'),
            ('Prof. Dr. H. Muhammad Sholahuddin, SE., Ph.D', 'Wakil Sekretaris'),
            ('Teguh Wahyudi, S.Sos', 'Bendahara'),
            ('Sri Mulyono, S.Pd., M.Si', 'Wakil Bendahara'),
        ]

        for nama, jabatan in daftar_pimpinan:
            Pimpinan.objects.update_or_create(
                nama=nama,
                defaults={
                    'jabatan': jabatan,
                    'periode': '2022–2027',
                }
            )

        # Data amal usaha pendidikan
        daftar_amal_usaha = [
            'SD Muhammadiyah 4 Kandangsapi Jebres',
            'SMP Muhammadiyah 7',
        ]

        for nama in daftar_amal_usaha:
            AmalUsaha.objects.update_or_create(
                nama=nama,
                defaults={
                    'bidang': AmalUsaha.Bidang.PENDIDIKAN,
                    'alamat': (
                        'Jalan Tentara Pelajar No. 1, '
                        'Kandangsapi, Jebres, Surakarta.'
                    ),
                }
            )

        # Tautan organisasi terkait
        daftar_tautan = [
            ('Muhammadiyah', 'https://muhammadiyah.or.id/'),
            ('Suara Muhammadiyah', 'https://suaramuhammadiyah.id/'),
            ('Lazismu', 'https://lazismu.org/'),
        ]

        for nama, url in daftar_tautan:
            TautanTerkait.objects.update_or_create(
                nama=nama,
                defaults={'url': url}
            )

        self.stdout.write(
            self.style.SUCCESS(
                'Data awal PCM Jebres berhasil dimasukkan!'
            )
        )
