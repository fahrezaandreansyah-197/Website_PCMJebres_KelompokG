# Menggunakan Python 3.14
FROM python:3.14-slim

# Mengatur direktori kerja
WORKDIR /app

# Menggunakan uv untuk mengelola dependensi
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Konfigurasi uv
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Menyalin file dependensi
COPY pyproject.toml uv.lock ./

# Menginstal dependensi berdasarkan uv.lock
RUN uv sync --frozen --no-dev --no-install-project

# Menyalin seluruh kode proyek
COPY . .

# Mengumpulkan file static Django
RUN SECRET_KEY=build-only DEBUG=False ALLOWED_HOSTS=localhost \
    .venv/bin/python manage.py collectstatic --noinput

# Membuat user non-root
RUN useradd --create-home appuser \
    && mkdir -p /app/media \
    && chown -R appuser:appuser /app

USER appuser

# Port aplikasi
EXPOSE 8000

# Menjalankan Django menggunakan Gunicorn
CMD ["sh", "-c", ".venv/bin/python manage.py migrate --noinput && .venv/bin/python manage.py seed_pcm && .venv/bin/gunicorn config.wsgi:application --bind 0.0.0.0:8000"]
