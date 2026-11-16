from django.urls import path
from . import views

app_name = 'publikasi'

urlpatterns = [
    path('berita/', views.daftar_berita, name='daftar_berita'),
    path('berita/<slug:slug>/', views.detail_berita, name='detail_berita'),
    path('agenda/', views.daftar_agenda, name='daftar_agenda'),
    path('unduhan/', views.daftar_dokumen, name='daftar_dokumen'),
]
