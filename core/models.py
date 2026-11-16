from django.db import models

class ProfilOrganisasi(models.Model):
    nama = models.CharField(max_length=200)
    nama_singkat = models.CharField(max_length=50)
    tagline = models.CharField(max_length=255, blank=True)
    tentang = models.TextField(blank=True)
    sejarah = models.TextField(blank=True)
    visi = models.TextField(blank=True)
    misi = models.TextField(blank=True)
    alamat = models.TextField()
    telepon = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    jumlah_anggota_ktam = models.PositiveIntegerField(default=0)
    gambar_utama = models.ImageField(
        upload_to='profil/',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Profil Organisasi'
        verbose_name_plural = 'Profil Organisasi'

    def __str__(self):
        return self.nama


class Pimpinan(models.Model):
    nama = models.CharField(max_length=150)
    jabatan = models.CharField(max_length=150)
    periode = models.CharField(max_length=20, default='2022–2027')
    foto = models.ImageField(upload_to='pimpinan/', blank=True, null=True)
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['urutan', 'nama']

    def __str__(self):
        return f'{self.nama} - {self.jabatan}'


class Ranting(models.Model):
    nama_ranting = models.CharField(max_length=150)
    ketua = models.CharField(max_length=150, blank=True)
    alamat = models.TextField(blank=True)
    telepon = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ['nama_ranting']

    def __str__(self):
        return self.nama_ranting


class AmalUsaha(models.Model):

    class Bidang(models.TextChoices):
        PENDIDIKAN = 'pendidikan', 'Pendidikan'
        KESEHATAN = 'kesehatan', 'Kesehatan'
        SOSIAL = 'sosial', 'Sosial'
        EKONOMI = 'ekonomi', 'Ekonomi'

    nama = models.CharField(max_length=200)
    bidang = models.CharField(
        max_length=20,
        choices=Bidang.choices
    )
    deskripsi = models.TextField(blank=True)
    alamat = models.TextField(blank=True)
    gambar = models.ImageField(
        upload_to='amal_usaha/',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['bidang', 'nama']

    def __str__(self):
        return self.nama


class TautanTerkait(models.Model):
    nama = models.CharField(max_length=100)
    url = models.URLField()
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['urutan', 'nama']

    def __str__(self):
        return self.nama

class MajelisLembaga(models.Model):
    nama_jabatan = models.CharField(max_length=200)
    nama_ketua = models.CharField(max_length=150)
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['urutan', 'nama_jabatan']
        verbose_name = 'Pimpinan Majelis dan Lembaga'
        verbose_name_plural = 'Pimpinan Majelis dan Lembaga'

    def __str__(self):
        return f'{self.nama_jabatan} - {self.nama_ketua}'