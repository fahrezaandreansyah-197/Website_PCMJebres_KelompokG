from django.db import models
# Model untuk menyimpan pesan dari pengunjung website
class PesanMasuk(models.Model):
    nama = models.CharField(max_length=150)
    email = models.EmailField()
    subjek = models.CharField(max_length=200)
    pesan = models.TextField()
    waktu_kirim = models.DateTimeField(auto_now_add=True)
    sudah_dibaca = models.BooleanField(default=False)

    class Meta:
        ordering = ['-waktu_kirim']
        verbose_name = 'Pesan Masuk'
        verbose_name_plural = 'Pesan Masuk'

    def __str__(self):
        return f'{self.nama} - {self.subjek}'
