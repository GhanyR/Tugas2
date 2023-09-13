# Tugas 2 Pemrograman Berbasis Platform (CSGE602022) - Semester Ganjil 2023/2024
## Fakultas Ilmu Komputer Universitas Indonesia
### Ghany Rasyid Prawira - NPM: 2206082392 - Kelas: PBP C

---

## Deskripsi Tugas
Implementasi konsep Model-View-Template (MVT) pada Django dengan tema aplikasi pengelolaan/Inventori.

## Fitur Aplikasi
- **Model**: Menggunakan model dengan nama `Item` yang memiliki atribut `name`, `amount`, dan `description`.
- **View**: Menampilkan nama aplikasi, nama, dan kelas.
- **Template**: Menggunakan template HTML untuk menampilkan data.

## Cara Menjalankan Aplikasi di Local
1. Aktifkan virtual environment: `source env/bin/activate` (Linux/Mac) atau `env\Scripts\activate` (Windows).
2. Masuk ke direktori proyek: `cd tugas1`
3. Jalankan server: `python manage.py runserver`

## Checklist
- [x] Membuat sebuah proyek Django baru.
- [x] Membuat aplikasi dengan nama `main`.
- [x] Melakukan routing.
- [x] Membuat model `Item`.
- [x] Membuat fungsi pada `views.py`.
- [x] Melakukan deployment ke Adaptable (opsional).

## Pertanyaan
1. **Step-by-step Implementasi**: Lihat pada bagian di bawah ini.
2. **Bagan Request dan Respon**: Sudah, Screenshot dibawah
3. **Virtual Environment**: Digunakan untuk isolasi dependensi, memudahkan manajemen paket.
4. **MVC, MVT, MVVM**: MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah pola desain yang berbeda dalam memanajemen aplikasi.

<img width="509" alt="image" src="https://github.com/GhanyR/Tugas2/assets/63539023/562eeb60-19da-419c-afed-0b268af2369c">

### Step-by-step Implementasi
1. Membuat proyek baru: `django-admin startproject tugas1`
2. Membuat aplikasi `main`: `python manage.py startapp main`
3. Update `settings.py` untuk menambahkan `main` di `INSTALLED_APPS`.
4. Buat model `Item` di `models.py`.
5. Buat fungsi `index` di `views.py`.
6. Update `urls.py` di aplikasi `main` dan proyek `tugas1`.
7. Jalankan migrasi: `python manage.py makemigrations` dan `python manage.py migrate`
8. Jalankan server: `python manage.py runserver`

### Akun Adaptable disabled, tidak bisa login
![image](https://github.com/GhanyR/Tugas2/assets/63539023/e780e403-fa50-4fbc-bb89-10bbff33ad32)


