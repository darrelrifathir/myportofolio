Nama : Darrel Rifathir Arwa
NPM  : 2506536420
Kelas: C

# My Portofolio
Repositori ini berisi kode untuk website (*static web*) pribadi, dibangun dengan Django (sebagai *server* dasar) serta HTML5 dan CSS3 untuk *interface* nya

# Tugas 1
## Progres Pekan ini dan Instruksi Setup Mingguan (31 Agustus &mdash; 7 September 2026):
Pada tugas pertama ini, saya telah menambahkan bagian *education* pada portofolio pribadi saya yang berisi riwayat pendidikan, disertai dengan deskripsinya. Berikut rincian mengenai hal-hal apa saya yang saya kembangkan pada pekan ini:
*   Menambahkan bagian **Education** (Riwayat Pendidikan) yang merender *cards* pengalaman secara rapi.
*   Menyematkan logo sekolah/universitas dengan rasio yang disesuaikan menggunakan *CSS properties* (`object-fit: contain`, pembungkus kotak putih melengkung).
*   Memperbaiki bug konfigurasi `ALLOWED_HOSTS` pada `settings.py` untuk memastikan kelancaran *deployment* ke PWS.

**Cara Instalasi dan Menjalankan Proyek Secara Lokal:**
1.  **Kloning repositori:**
    ```bash
    git clone [https://github.com/darrelrifathir/myportofolio.git](https://github.com/darrelrifathir/myportofolio.git)
    cd myportofolio
    ```
2.  **Buat dan aktifkan *Virtual Environment*:**
    ```bash
    python -m venv env
    # Pengguna Windows:
    env\Scripts\activate
    # Pengguna macOS/Linux:
    source env/bin/activate
    ```
3.  **Instalasi *dependencies*:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Jalankan migrasi database:**
    ```bash
    python manage.py migrate
    ```
5.  **Jalankan server lokal:**
    ```bash
    python manage.py runserver
    ```
    Buka `http://127.0.0.1:8000/` di *browser* Anda.

---

## Jawaban Pertanyaan Reflektif
### 1. Penggunaan Elemen Semantik HTML5
Ya, dalam merancang struktur antarmuka portofolio ini, saya menggunakan elemen semantik HTML5 seperti <section>, dan <article>. Penggunaan elemen semantik ini sangat membantu saya dalam memberikan makna yang sebenarnya pada dokumen *static web*. Sebagai contoh, saya menggunakan tag <section> untuk memisahkan area profil dan pendidikan. Selain itu, saya menggunakan tag <article> untuk membungkus setiap entri *cards* di bagian pendidikan (contoh: <article class="edu-card">). Hal ini tidak hanya mempermudah keterbacaan kode dengan menghindari penumpukan tag <div> yang terlalu generik, tetapi juga memastikan mesin pencari dapat mengidentifikasi bagian tersebut sebagai konten yang saling berdiri sendiri.

### 2.  Tantangan Tata Letak Responsif (Desktop ke Mobile)
Tantangan tata letak yang terbesar bagi saya adalah memastikan struktur grid tidak saling bertumpuk saat diakses melalui layar kecil. Untuk bagian hero, saya menggunakan properti media query @media (max-width: 600px) untuk merombak .hero-grid yang awalnya memiliki dua kolom (1.3fr 1fr) menjadi satu kolom vertikal penuh (1fr). Saya juga memprioritaskan penyusutan ukuran foto profil dengan membatasi .hero-photo pada lebar maksimum 220px agar tidak mendominasi layar mobile. Sementara itu, untuk meminimalisasi tantangan tata letak pada bagian pendidikan, saya  menggunakan grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) pada .edu-grid. Ini memungkinkan kartu-kartu pendidikan secara otomatis menyesuaikan ukuran dan berpindah baris mengikuti lebar *viewport* tanpa perlu memaksakan perubahan posisi secara manual.  

### 3. Batasan Static Web dan Rencana Fungsionalitas Dinamis
Batasan utama dari static web murni ini adalah tidak adanya skalabilitas dan interaktivitas data dari sisi servernya. Saat ini, seluruh informasi penting seperti detail kontak, deskripsi profil, dan riwayat pendidikan hanya diketik secara langsung (hardcoded) di dalam berkas index.html. Jika saya ingin memperbarui bio atau menambah pengalaman baru, saya harus mengubah baris kode HTML secara manual. Berdasarkan batasan tersebut, fungsionalitas dinamis yang paling ingin saya tambahkan pada pembaruan proyek yang selanjutnya adalah dengan mengimplementasi basis data melalui framework Django. Saya berencana memindahkan data portofolio ke dalam database agar bisa dikelola melalui panel admin, sehingga antarmuka web hanya bertugas merender template secara dinamis tanpa perlu menyentuh source code HTML lagi.

---

## AI Disclosure & Log Prompting

Dalam pengembangan tugas ini, saya menggunakan asisten AI (Gemini) sebagai partner diskusi untuk hal-hal bersifat teknis. 

*   **Tools yang Digunakan:** Gemini 3.1 Pro
*   **Strategi Prompting:** Saya tidak meminta AI membuat kode html atau syle.css nya secara langsung, melainkan saya memberikan cuplikan kode CSS, *screenshot* kendala visual (seperti rasio gambar yang pecah), atau log *error* terminal secara spesifik untuk dipecahkan bersama.
*   **Bagian Spesifik yang Dibantu AI:**
    *   Penyesuaian properti *flexbox* dan `object-fit` pada CSS untuk membungkus gambar logo multi-format (PNG/JPG) ke dalam kartu profil.
    *   Mendiagnosis masalah ketidakcocokan *branch* Git (`master` vs `main`) saat proses *push* ke repositori.
    *   Pembuatan kerangka pesan *commit* yang mematuhi standar *Conventional Commits*.
*   **Analisis Kritis Keterbatasan AI & Perbaikan Manual:** 
    AI memberikan solusi teknis yang tepat seperti penggunaan `mix-blend-mode: multiply` untuk menyatukan latar belakang gambar dengan kontainer. Namun, AI memiliki keterbatasan dalam merasakan proporsi estetika dan keselarasan tema warna secara visual. Pada awalnya, AI menyarankan tinggi kotak yang terlalu besar (`150px`) dan latar belakang putih murni (`#ffffff`). Sebagai perbaikan manual, saya secara mandiri menyusutkan `height` kontainer menjadi `110px` agar logo fit tanpa ruang kosong. Selain itu, saya juga menyesuaikan `background-color` kotak menjadi `rgba(28, 25, 23, 0.04)` dibandingkan hanya warna putih, agar lebih membaur dengan palet warna desain portofolio saya secara keseluruhan.
*   **Log Prompting:**
    *   *Prompt 1:* "why is it not showing? [Melampirkan *screenshot* ikon *broken image* pada HTML]"
        *   *Respons AI:* AI mendiagnosis bahwa gambar tidak muncul karena kemungkinan ada kesalahan penulisan nama berkas (seperti perbedaan spasi atau huruf kapital) atau jalur folder pada atribut `src` di tag `<img>`.
    *   *Prompt 2:* "how do i fit it in the box correctly? [Melampirkan *screenshot* rasio logo UI dan logo SMAN 3 yang berantakan]"
        *   *Respons AI:* AI menyarankan penambahan kelas `.edu-img-box` dengan `display: flex` dan `.edu-logo` dengan `object-fit: contain`. Properti ini berfungsi untuk memaksa gambar menyesuaikan diri ke dalam rasio kotak tanpa membuatnya terdistorsi atau gepeng.
    *   *Prompt 3:* "oke gw udah bisa gambarnya, tapi i think ini keknya kotaknya kegedean gak sih? Agak kecilin kotaknya dong biar dia tetep fit [Melampirkan *screenshot* kotak logo yang terlalu banyak ruang kosong]"
        *   *Respons AI:* AI memberikan revisi CSS untuk menyesuaikan tinggi kotak dengan menyarankan perubahan nilai `height` menjadi `110px` dan `padding` menjadi `1rem` pada class `.edu-img-box` agar kontainer lebih bagus dalam membungkus logo univ/sekolah.

# Tugas 2
## Jawaban Pertanyaan Reflektif

### 1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.
Alur arsitektur MVT (Model-View-Template) saat pengguna membuka halaman yang saya buat, `/certification/` adalah sebagai berikut:
* **Request:** Browser mengirimkan HTTP Request ke server web.
* **urls.py proyek (`portofolio/urls.py`):** Bertindak sebagai *router* utama. Ia menerima request dan meneruskannya ke *router* spesifik aplikasi `main` menggunakan `include('main.urls')`.
* **urls.py aplikasi (`main/urls.py`):** Mencocokkan *path* `/certification/` dengan fungsi *named route* dan meneruskannya ke fungsi *view* yang tepat, yaitu `show_certification`.
* **View (`views.py`):** Berperan seperti jembatan untuk fungsi `show_certification` agar ia memanggil Model untuk meminta data.
* **Model (`models.py`):** Bertugas mengambil data objek-objek `Certification` dari *database*, lalu mengembalikannya ke View.
* **Template (`certification.html`):** View membungkus data tersebut ke dalam *context* dan memberikannya ke Template. Template kemudian memproses data menggunakan *Django Template Language* (seperti `{% for %}`) untuk merender struktur HTML secara dinamis.
* **Response:** HTML yang sudah dirender beserta datanya dikembalikan oleh View sebagai HTTP Response untuk ditampilkan di browser pengguna.

### 2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.
Menyimpan data pada Model bertujuan untuk memisahkan antara logika data dan dari segi UI. Dengan menyimpan data pada model, akan berdampak kepada kemudahan pemeliharaan dan pengembangan aplikasi yang cukup signifikan:
* **Kemudahan Pemeliharaan:** Jika saya ingin menambah, mengubah, atau menghapus sertifikasi baru, saya hanya perlu mengubah isi *database*  melalui Django shell tanpa perlu menyentuh atau mengedit teks secara *hard-coded* di file HTML yang ingin saya tambahkan. 
* **Skalabilitas:** Template HTML cukup ditulis satu kali menggunakan perulangan, memudahkan saya untuk mengakses banyak data terutama jika ukuran data nya sangat besar, sehingga kode template html tidak terlalu panjang dan terlihat lebih *clean*.

### 3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.
* **`makemigrations`:** Berfungsi untuk mendeteksi perubahan pada object **Class** di `models.py` dan membuatkan *file blueprint* migrasi baru yang mencatat rencana perubahan tersebut. Perintah ini belum mengubah *database* sama sekali.
* **`migrate`:** Berfungsi untuk menerapkan perubahan yang tercatat di dalam *file blueprint* migrasi ke dalam *database* sesungguhnya (mengeksekusi SQL untuk membuat/mengubah tabel).

* **Contoh Kasus pada nomer 3**:
Ketika saya menambahkan field baru `thumbnail = models.CharField(...)` pada model `Certification` yang sudah ada, saya harus menjalankan `makemigrations` agar Django membuat file migrasi yang mencatat penambahan kolom tersebut. Setelah itu, saya menjalankan `migrate` agar tabel `main_certification` di dalam *database* benar-benar diperbarui dengan kolom `thumbnail` yang baru.

## AI Disclosure & Log Prompting
Dalam mengerjakan tugas 2 ini, saya menggunakan asisten AI (Gemini) sebagai partner diskusi untuk hal-hal bersifat teknis. 

*   **Tools yang Digunakan:** Gemini 3.1 Pro
*   **Strategi Prompting:** Saya tidak meminta AI menulis seluruh kode dari awal, melainkan meminta panduan langkah demi langkah sesuai *checklist* MVT Django, serta memberikan log *error*, potongan kode (seperti penggunaan Django Shell), atau *screenshot* saat mengalami kendala teknis agar dapat kita pecahkan bersama.
*   **Bagian Spesifik yang Dibantu AI:**
    *   Pemecahan masalah asinkronisasi data antara *database* lokal (`db.sqlite3`) dengan server PWS.
    *   Debugging gambar *broken link* dari *image hosting* pihak ketiga dan transisi ke penyimpanan *static* di lokal.
    *   Penyelesaian masalah duplikasi data (*Multiple Objects Returned*) pada Django ORM di terminal.
*   **Analisis Kritis Keterbatasan AI & Perbaikan Manual:** 
    Pada saat saya ingin menambahkan fitur `thumbnail` pada sertifikasi, AI awalnya menyarankan penggunaan `URLField` untuk menyimpan tautan gambar dari *image hosting* eksternal. Namun, AI kurang mengantisipasi restriksi *hotlinking* dan kesulitan ekstraksi *direct link* dari platform seperti ImgBB yang menyebabkan gambar tetap rusak (*broken image*) saat dirender di HTML. Menyadari keterbatasan tersebut, saya mengambil keputusan manual untuk mengabaikan penggunaan *URL hosting* luar. Saya merombak model `thumbnail` menjadi `CharField`, melakukan migrasi ulang, dan memindahkan aset gambar secara manual ke dalam direktori lokal `/static/img/` proyek agar aset terjamin dapat diakses tanpa bergantung pada server eksternal.
*   **Log Prompting:**
    *   *Prompt 1:* "gw udah push, tapi kok experience nya gaada lagi kalo gw liat di PWS? tapi kalo gw buka http localhost 8000 sendiri itu masih ada [Melampirkan screenshot halaman PWS yang isi experiencenya kosong]"
        *   *Respons AI:* AI menjelaskan bahwa file `db.sqlite3` masuk ke dalam `.gitignore` sehingga data lokal tidak ikut ter-*push* ke PWS. AI meyakinkan bahwa kondisi ini normal karena server produksi PWS membuat *database* baru yang masih kosong.
    *   *Prompt 2:* "Ini kenapa begini ya? gw jadinya pake imgbb buat host gambar tapi kek gini jadinya [Melampirkan screenshot logo *broken image* pada card Certification]"
        *   *Respons AI:* AI mendiagnosis bahwa tag `<img>` di HTML gagal merender gambar karena URL yang dimasukkan adalah halaman *viewer* ImgBB, bukan *direct link* (tautan langsung berakhiran .jpg/.png), lalu mencoba memandu cara mengekstrak *link* tersebut.
    *   *Prompt 3:* "oke gw udah migrate tapi masalahnya udah gw tambahin object baru, bukannya malah hapus objek yg lama. Title nya sama lagi, gimana hapus yg sebelumnya?"
        *   *Respons AI:* AI mendiagnosis bahwa karena ada dua objek dengan judul yang sama, akan memicu *error* `MultipleObjectsReturned` ke depannya. AI memberikan solusi query `Certification.objects.filter(...).delete()` melalui Django Shell untuk membersihkan data duplikat secara aman sebelum membuat ulang objek finalnya.