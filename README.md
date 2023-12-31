# Tugas 2, 3, 4, 5, dan 6 Pemrograman Berbasis Platform (CSGE602022) - Semester Ganjil 2023/2024
## Fakultas Ilmu Komputer Universitas Indonesia
### Ghany Rasyid Prawira - NPM: 2206082392 - Kelas: PBP C

---

## Deskripsi Tugas
Implementasi konsep Model-View-Template (MVT) pada Django dengan tema aplikasi pengelolaan/Inventori.

## Fitur Aplikasi
- **Model**: Menggunakan model dengan nama `Item` yang memiliki atribut `name`, `amount`, dan `description`.
- **View**: Menampilkan nama aplikasi, nama, dan kelas.
- **Template**: Menggunakan template HTML untuk menampilkan data.

----

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

----

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

---

# Tugas 3 
### Ghany Rasyid Prawira - NPM: 2206082392 - Kelas: PBP C

---

## Deskripsi Tugas
Implementasi form dan data delivery pada Django dengan tema aplikasi pengelolaan Inventaris. 

## Fitur Aplikasi
- **Input Form**: Membuat form input untuk menambahkan item pada inventaris.
- **Display Item**: Menampilkan item yang telah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
- **URL Routing**: Melakukan routing untuk setiap views.
- **Postman Access**: Mengakses setiap URL menggunakan Postman dan melakukan screenshot.

## Checklist
- [x] Membuat input form untuk menambahkan item.
- [x] Menambahkan fungsi untuk melihat item yang telah ditambahkan.
- [x] Melakukan routing untuk setiap fungsi.
- [x] Menjawab pertanyaan yang diberikan.
- [x] Mengakses semua URL menggunakan Postman dan melakukan screenshot.
- [x] Melakukan add-commit-push ke GitHub.

## Pertanyaan
1. **Pembeda Form POST dan GET Django**: Form POST digunakan jika kita ingin mengirimkan data ke server sementara Form GET digunakan jika kita ingin mendapatkan data dari server.
2. **Perbedaan XML, JSON, dan HTML**: XML dan JSON digunakan untuk menyimpan dan mengirimkan data sementara HTML digunakan untuk menampilkan data. JSON lebih sederhana dan mudah dibaca dibandingkan XML.
3. **Penggunaan JSON**: JSON digunakan dalam pertukaran data karena formatnya ringkas dan mudah dibaca oleh manusia dan mesin.
4. **Implementasi Checklist**: Lihat di bawah ini.

<img width="509" alt="image" src="https://github.com/GhanyR/Tugas3/assets/63539023/562eeb60-19da-419c-afed-0b268af2369c">

### Step-by-step Implementasi
1. Membuat form input: `forms.py`
2. Menambahkan fungsi `AddItem` dan `ViewItem` di `views.py`.
3. Update `urls.py` untuk melakukan routing ke setiap fungsi.
4. Membuat view untuk menampilkan data dalam XML dan JSON.
5. Mengakses setiap URL menggunakan Postman dan melakukan screenshot.
6. Melakukan add-commit-push ke GitHub.

---

# Tugas 4
### Ghany Rasyid Prawira - NPM: 2206082392 - Kelas: PBP C

---

## Deskripsi Tugas
Implementasi konsep authentication, session, dan cookies pada Django dengan tema aplikasi pengelolaan/Inventori. Selain itu, juga mengimplementasikan konsep lain yang telah diajarkan selama sesi tutorial.

## Fitur Aplikasi
- **User Authentication**: Menyediakan fungsi registrasi, login, dan logout.
- **User Account**: Menciptakan dua tipe akun pengguna dengan masing-masing tiga dummy data.
- **User-Item Relation**: Menyambungkan model Item dengan User.
- **User Information**: Menampilkan detail dari pengguna yang sedang login seperti username dan last login cookies.

## Checklist
- [x] Membuat fungsi registrasi, login, dan logout.
- [x] Menciptakan dua akun pengguna dengan masing-masing tiga dummy data.
- [x] Menyambungkan model Item dengan User.
- [x] Menampilkan informasi pengguna yang sedang login.
- [x] Menerapkan cookies ke aplikasi.
- [x] Melakukan add-commit-push ke Github.

## Pertanyaan
1. **Django UserCreationForm**: Django UserCreationForm adalah form yang disediakan oleh Django untuk proses pendaftaran. Kelebihannya adalah mengurangi waktu pengembangan dan memperjelas proses validasi. Namun, kurangnya fleksibilitas dalam menyesuaikan fungsi dan tampilan menjadi kekurangan dari UserCreationForm.
2. **Autentikasi vs Otorisasi**: Autentikasi dalam konteks Django adalah proses verifikasi identitas pengguna saat login, sedangkan otorisasi adalah proses verifikasi hak akses pengguna berdasarkan identitas yang sudah diverifikasi. Kedua elemen ini penting karena autentikasi akan memastikan bahwa user yang akses adalah benar user tersebut dan otorisasi membatasi akses user sesuai dengan hak aksesnya.
3. **Cookies dan Django**: Cookies dalam konteks aplikasi web digunakan untuk menyimpan informasi pengguna dalam browser agar pengguna tidak perlu masuk secara berulang. Django menggunakan cookies untuk mengelola data sesi pengguna dan pembuatan cookies di Django dapat dilakukan dengan HttpResponse.set_cookie() method.
4. **Penggunaan Cookies**: Penggunaan cookies secara umum aman dalam pengembangan web tetapi ada beberapa risiko potensial yang harus diwaspadai, seperti cookies dapat disalahgunakan oleh hacker untuk mencuri informasi yang dapat digunakan untuk tujuan jahat.
5. **Step-by-step Implementasi**: Lihat di bagian bawah.

## Step-by-step Implementasi
1. Mengaktifkan module User django dan membuat form registrasi dan login di `forms.py`.
2. Membuat fungsi untuk proses register, login, dan logout di `views.py`.
3. Membuat dua akun dummy data dan menjalankan migrasi database.
4. Menyambungkan model Item dengan User dengan melakukan penyesuaian di `models.py`.
5. Menunjukkan detail pengguna melalui template dan menggunakan cookies untuk menyimpan data last login.


## Bonus
### Tambahan Fitur
- **Item Manipulation Buttons and Functions**: Menambahkan tombol dan fungsional untuk menambah dan mengurangi jumlah item serta menghapus item dari inventori.

## Implementasi Bonus
- [x] Menambahkan tombol dan fungsi "add"/"substract" item amount dan fungsi "delete" item.

---

# Tugas 5
### Ghany Rasyid Prawira - NPM: 2206082392 - Kelas: PBP C

---

## Deskripsi Tugas
Desain Web menggunakan HTML, CSS dan Framework CSS untuk mengimplementasikan desain web berdasarkan beberapa hal yang sudah dipelajari selama tutorial (CSS, Framework, dsb).

## Fitur Aplikasi
- **Kustomisasi Desain**: Mengkustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma).
- **Kustomisasi Halaman**: Mengkustomisasi halaman login, register, dan tambah inventori serta halaman daftar inventori.

## Checklist
- [x] Kustomisasi desain pada templat HTML menggunakan CSS atau CSS framework.
- [x] Kustomisasi halaman login, register, dan tambah inventori.
- [x] Kustomisasi halaman daftar inventori.
- [x] Menjawab pertanyaan yang diberikan pada README.md.
- [x] Melakukan add-commit-push ke Github.

## Pertanyaan
1. **Element Selector dan Pemanfaatannya**: Element selector digunakan untuk memilih elemen berdasarkan tipe elemen nya. Manfaatnya bisa digunakan untuk memilih sebuah elemen dan mengaplikasikan style CSS yang sama pada setiap elemen tersebut. 
2. **Tag HTML5**: beberapa tag HTML5 yang saya ketahui antara lain: `<header>, <footer>, <article>, <section>, <nav>, <aside>, <figure>, and <figcaption>`.
3. **Perbedaan Margin dan Padding**: Margin adalah jarak antara elemen dengan elemen lain disekitarnya, sedangkan padding adalah jarak antara konten dalam elemen dengan batas elemen itu sendiri.
4. **Perbedaan Framework CSS Tailwind dan Bootstrap**: Bootstrap adalah  CSS Framework yang menyediakan fitur dan style siap pakai, sedangkan Tailwind adalah CSS Framework yang memanggil class melalui HTML. Tailwind memberikan kontrol yang lebih besar terhadap detail desain sedangkan Bootstrap biasanya digunakan untuk mempercepat proses pembuatan website menggunakan component yang sudah disediakan.
5. **Step-by-step Implementasi**: Lihat di bagian bawah.

## Step-by-step Implementasi
1. Memilih Framework CSS, dalam hal ini saya memilih Bootstrap.
2. Menambahkan stylesheet Bootstrap ke file HTML.
3. Melakukan kustomisasi pada halaman login, register, dan tambah inventori menggunakan class yang ada di Bootstrap.
4. Melakukan kustomisasi pada halaman daftar inventori menggunakan class yang ada di Bootstrap, dan mengubah tampilan tabel menjadi menggunakan card.
5. Melakukan pengecekan dan memastikan semua telah berjalan dengan baik.

## Bonus
### Tambahan Fitur
Menerapkan warna yang berbeda (teks atau background) pada baris terakhir dari item inventori menggunakan CSS.

## Implementasi Bonus
- [x] Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari item pada inventori anda menggunakan CSS. 

---

# Tugas 6: JavaScript dan Asynchronous JavaScript
### Ghany Rasyid Prawira - NPM: 2206082392 - Kelas: PBP C

---

## Deskripsi Tugas
Pada tugas ini, kamu akan mengimplementasikan AJAX pada aplikasi yang telah kamu buat pada tugas sebelumnya.

### Checklist:
- [x] Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
- [x] AJAX GET: Ubah kode cards data item untuk mendukung AJAX GET dan pengambilan task menggunakan AJAX GET.
- [x] AJAX POST: Buat tombol untuk modal dengan form untuk menambahkan item dan refresh halaman utama secara asinkronus setelah penambahan.
- [x] Melakukan perintah `collectstatic` untuk mengumpulkan file static.
- [x] Menambahkan jawaban pertanyaan pada README.md dan melakukan add-commit-push ke GitHub.
- [x] Melakukan deployment ke PaaS PBP Fasilkom UI dan sertakan tautan aplikasi pada file README.md.
- [x] DOKKU_APP_NAME = UsernameSSO-tugas (Contoh: muhammad-iqbal111-tugas).

## Pertanyaan:

1. **Asynchronous vs Synchronous Programming**: 
   
   Asynchronous programming memungkinkan komputer untuk menjalankan tugas lainnya sementara menunggu operasi lain selesai. Sementara itu, synchronous programming mengeksekusi kode dalam urutan yang ditentukan, sehingga komputer menunggu tugas satu selesai sebelum pindah ke yang berikutnya.

2. **Event-driven Programming pada JavaScript & AJAX**: 

   Event-driven programming adalah suatu pendekatan dimana flow program ditentukan oleh peristiwa seperti input user atau I/O operations. Contoh penerapannya pada tugas ini adalah ketika user menekan tombol untuk menambahkan item, AJAX POST request akan dipicu.

3. **Asynchronous Programming pada AJAX**: 

   AJAX memungkinkan web page untuk memperbarui tanpa harus me-refresh seluruh halaman. Menggunakan AJAX, JavaScript dapat berkomunikasi dengan server, mengambil data, dan memperbarui web page tanpa melakukan refresh.

4. **Fetch API vs jQuery untuk AJAX**: 

   Fetch API adalah modern way untuk melakukan AJAX request yang dibuat oleh browser vendors sedangkan jQuery adalah library yang menyediakan AJAX melalui method seperti $.ajax(). Fetch API lebih modern dan native sedangkan jQuery memerlukan library tambahan. Menurut saya, Fetch API lebih baik untuk penggunaan modern tetapi jQuery masih berguna untuk keperluan backward compatibility.

5. **Implementasi Checklist**:

   a. Mengubah desain halaman agar mendukung AJAX.
   
   b. Mengimplementasikan AJAX GET untuk mengambil data item.
   
   c. Mengimplementasikan AJAX POST untuk menambahkan item ke database.
   
   d. Membuat modal dengan form untuk input item.
   
   e. Mengimplementasikan refresh asinkronus setelah penambahan item.
   
   f. Melakukan perintah `collectstatic` untuk mengumpulkan file static.

---

## Bonus
### Fitur Tambahan:
- [x] Menambahkan fungsionalitas hapus menggunakan AJAX DELETE.
