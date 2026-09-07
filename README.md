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