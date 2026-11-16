from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class BeritaQuerySet(models.QuerySet):
    def terbit(self):
        return self.filter(
            status='terbit',
            tanggal_terbit__lte=timezone.now()
        )

class BeritaManager(models.Manager.from_queryset(BeritaQuerySet)):
    pass
# Model untuk menyimpan berita PCM Jebres
class Berita(models.Model):
    objects = BeritaManager()
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        TERBIT = 'terbit', 'Terbit'

    judul = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    ringkasan = models.TextField()
    isi = models.TextField()
    gambar_sampul = models.ImageField(
        upload_to='berita/',
        blank=True,
        null=True
    )
    tanggal_terbit = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )

    class Meta:
        ordering = ['-tanggal_terbit']

    def save(self, *args, **kwargs):
        if not self.slug:
            dasar_slug = slugify(self.judul)
            slug = dasar_slug
            nomor = 1

            while Berita.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{dasar_slug}-{nomor}'
                nomor += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.judul


# Model untuk menyimpan agenda kegiatan
class Agenda(models.Model):
    nama_kegiatan = models.CharField(max_length=200)
    waktu_mulai = models.DateTimeField(
    blank=True,
    null=True,)
    jadwal_rutin = models.CharField(
        max_length=150,
        blank=True,)
    tempat = models.CharField(max_length=200)
    keterangan = models.TextField(blank=True)

    class Meta:
        ordering = ['waktu_mulai']

    def __str__(self):
        return self.nama_kegiatan


# Model untuk menyimpan dokumen yang dapat diunduh
class Dokumen(models.Model):
    judul = models.CharField(max_length=200)
    keterangan = models.TextField(blank=True)
    file = models.FileField(upload_to='dokumen/')
    tanggal_unggah = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-tanggal_unggah']

    def __str__(self):
        return self.judul
