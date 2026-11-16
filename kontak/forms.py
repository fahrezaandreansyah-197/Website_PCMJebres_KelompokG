from django import forms
from .models import PesanMasuk


# Formulir untuk menerima pesan dari pengunjung
class PesanMasukForm(forms.ModelForm):

    class Meta:
        model = PesanMasuk
        fields = ['nama', 'email', 'subjek', 'pesan']

        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama lengkap',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan alamat email',
            }),
            'subjek': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan subjek pesan',
            }),
            'pesan': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Tuliskan pesan Anda',
            }),
        }
