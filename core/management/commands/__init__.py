import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Membuat superuser otomatis jika belum ada'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv('ADMIN_USERNAME', 'admin')
        email = os.getenv('ADMIN_EMAIL', 'admin@pcmjebres.com')
        password = os.getenv('ADMIN_PASSWORD', 'AdminPCM2026!')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" berhasil dibuat!'))
            self.stdout.write(self.style.SUCCESS(f'Password: {password}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" sudah ada.'))
