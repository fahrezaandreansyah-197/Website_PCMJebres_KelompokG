from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('profil/', views.profil, name='profil'),
    path('pimpinan/', views.pimpinan, name='pimpinan'),
    path('ranting/', views.ranting, name='ranting'),
    path('amal-usaha/', views.amal_usaha, name='amal_usaha'),
]