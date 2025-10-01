# Django Portfolio Production Setup (Docker)

## Prasyarat

-   Docker & Docker Compose
-   Git
-   Sudah memiliki container/database MySQL dan network Docker external (misal: mydbnet)

## Instalasi & Menjalankan

1. **Clone repository**

    ```bash
    git clone <repo-url>
    cd portofolio
    ```

2. **Buat file environment**

    ```bash
    cp .env.example .env
    # Edit .env sesuai kebutuhan (DB, SECRET_KEY, dsb)
    # Contoh konfigurasi MySQL:
    # DB_ENGINE=mysql
    # DB_NAME=namadb
    # DB_USER=userdb
    # DB_PASSWORD=passdb
    # DB_HOST=host_mysql
    # DB_PORT=3306
    ```

3. **Build & Jalankan dengan Docker Compose**

    ```bash
    docker-compose up --build
    ```

4. **Migrasi database & collectstatic**
   Buka terminal baru, lalu:

    ```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py collectstatic --noinput
    docker-compose exec web python manage.py seed_data
    ```

5. **Akses aplikasi**
   Buka browser ke: [http://localhost:8000](http://localhost:8000)

## Struktur Penting

-   `docker-compose.yml` : Orkestrasi service web (terhubung ke network eksternal MySQL)
-   `Dockerfile` : Build image Django + Gunicorn
-   `.env` : Konfigurasi environment (tidak di-commit)
-   `requirements.txt` : Daftar dependensi Python

## Catatan

-   Database MySQL DIHARAPKAN sudah berjalan di network Docker external (lihat `docker-compose.yml`)
-   Untuk development, gunakan Django runserver tanpa Gunicorn
-   Untuk production, pastikan DEBUG=False dan SECRET_KEY aman

---

**Happy deploying!**
