# Django Portfolio Production Setup (Docker)

## Prasyarat

-   Docker & Docker Compose
-   Git
-   Sudah memiliki container/database MySQL dan network Docker external (misal: mydbnet)

## Database Otomatis: SQLite (dev) & MySQL (production)

-   Secara default, project menggunakan SQLite untuk development (cukup jalankan tanpa konfigurasi DB tambahan).
-   Untuk production, atau jika ingin menggunakan MySQL, set DB_ENGINE=mysql dan isi variabel DB lain di file `.env`.

## Instalasi & Menjalankan

1.  **Clone repository**

    ```bash
    git clone <repo-url>
    cd portofolio
    ```

2.  **Buat file environment**

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
    # Untuk development, cukup biarkan DB_ENGINE=sqlite
    ```

3.  **Build & Jalankan dengan Docker Compose**

    ```bash
    docker-compose up --build
    ```

4.  **Migrasi database & collectstatic**
    Buka terminal baru, lalu:

    ```bash
    sudo docker compose exec web python manage.py generate_secret_key
    sudo docker compose exec web python manage.py migrate
    sudo docker compose exec web python manage.py collectstatic --noinput
    sudo docker compose exec web python manage.py seed_data
    sudo docker compose exec web python manage.py createsuperuser
    ```

    > Pastikan database MySQL sudah berjalan dan dapat diakses dari container web sebelum menjalankan migrate!

5.  **Akses aplikasi**
    Buka browser ke: [http://localhost:8000](http://localhost:8000)

## Struktur Penting

-   `docker-compose.yml` : Orkestrasi service web (terhubung ke network eksternal MySQL)
-   `Dockerfile` : Build image Django + Gunicorn
-   `.env` : Konfigurasi environment (tidak di-commit)
-   `requirements.txt` : Daftar dependensi Python

## Catatan

-   Untuk development, cukup gunakan SQLite (default, tanpa setting DB apapun).
-   Untuk production, gunakan MySQL dan pastikan variabel DB di `.env` sudah benar.
-   Untuk Windows + MySQL: install Visual C++ build tools jika error saat install mysqlclient.
-   Tidak ada lagi service db Postgres di docker-compose.
-   Untuk production, pastikan DEBUG=False dan SECRET_KEY aman.

## Troubleshooting

-   Jika gagal konek ke MySQL:
    -   Pastikan network Docker eksternal sudah benar dan MySQL sudah running.
    -   Cek ulang DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT di `.env`.
    -   Cek log container dengan `docker-compose logs web`.
-   Jika migrate gagal, pastikan MySQL sudah siap menerima koneksi.

---

**Happy deploying!**
