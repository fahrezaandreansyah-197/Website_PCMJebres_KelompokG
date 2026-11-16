from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PesanMasukForm

# Menampilkan halaman kontak dan memproses pesan pengunjung
def kontak(request):
    if request.method == 'POST':
        form = PesanMasukForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Pesan Anda berhasil dikirim. Terima kasih!'
            )
            return redirect('kontak:kontak')
    else:
        form = PesanMasukForm()

    return render(request, 'kontak/kontak.html', {
        'form': form,
    })
