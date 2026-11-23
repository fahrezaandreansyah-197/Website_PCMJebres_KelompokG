
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

# Membuat user non-root dan direktori penyimpanan
RUN useradd --create-home appuser \
    && mkdir -p /app/media /app/staticfiles /app/manifest \
    && chown -R appuser:appuser /app

# Menggunakan user non-root
USER appuser

# Port aplikasi
EXPOSE 8000

# Mengumpulkan static files dan menjalankan Django
CMD ["sh", "-c", ".venv/bin/python manage.py collectstatic --noinput && .venv/bin/python manage.py migrate --noinput && .venv/bin/python manage.py seed_pcm && .venv/bin/python manage.py init_admin && .venv/bin/gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]
