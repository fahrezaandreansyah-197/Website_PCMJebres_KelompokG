from django.test import TestCase
from django.urls import reverse

class HalamanUtamaTests(TestCase):

    def test_halaman_beranda(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_halaman_profil(self):
        response = self.client.get(reverse('core:profil'))
        self.assertEqual(response.status_code, 200)

    def test_halaman_pimpinan(self):
        response = self.client.get(reverse('core:pimpinan'))
        self.assertEqual(response.status_code, 200)

    def test_halaman_ranting(self):
        response = self.client.get(reverse('core:ranting'))
        self.assertEqual(response.status_code, 200)

    def test_halaman_amal_usaha(self):
        response = self.client.get(reverse('core:amal_usaha'))
        self.assertEqual(response.status_code, 200)
