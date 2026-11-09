Nama : Darrel Rifathir Arwa
NPM  : 2506536420
Kelas: C

# My Portofolio
Repositori ini berisi kode untuk website (*static web*) pribadi, dibangun dengan Django (sebagai *server* dasar) serta HTML5 dan CSS3 untuk *interface* nya

# Tugas 1
## Progres Pekan ini dan Instruksi Setup Mingguan (31 Agustus - 7 September 2026):
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

# Tugas 3
## Jawaban Pertanyaan Reflektif

### 1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan `{% csrf_token %}` pada form tersebut!
Kita menggunakan `ModelForm` karena jauh lebih efisien dan mengurangi repetisi kode secara terus-menerus. Django akan secara otomatis *men-generate* tag `<input>` HTML berdasarkan struktur model yang sudah kita buat, sehingga kita tidak perlu membuat form manual dari nol. Selain itu, `ModelForm` secara otomatis menangani logika validasi data dan mempermudah proses penyimpanan data langsung ke database melalui `form.save()`. 
Kita diwajibkan menggunakan `{% csrf_token %}` sebagai sistem keamanan bawaan Django untuk mencegah serangan CSRF (*Cross-Site Request Forgery*). Token unik ini memastikan bahwa data form yang dikirim (request `POST`) benar-benar berasal dari *website* kita sendiri, bukan dari situs lain yang memalsukan identitas misalnya. Tanpa token ini, Django akan memblokir form dan menghasilkan *error 403 Forbidden*.

### 2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?
JSON (*JavaScript Object Notation*) lebih disukai karena strukturnya jauh lebih sederhana dan mudah dibaca oleh manusia. JSON hanya menggunakan pasangan *key-value*, mirip seperti struktur *dictionary* di Python. Sebaliknya, XML mengharuskan penggunaan tag pembuka dan penutup yang bersarang (seperti HTML) sehingga membuat ukuran file menjadi lebih "berat" dan panjang. Karena JSON lebih ringan, transmisi datanya melalui jaringan menjadi lebih cepat.

### 3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?
Alurnya dimulai ketika pengguna atau aplikasi meminta data ke *endpoint* dari suatu URL tertentu (contoh: `/api/certifications/`). *Router* (`urls.py`) akan meneruskan *request* tersebut ke fungsi *view* yang sedang mengerjakan tugasnya (misal: `get_certifications_json`). Di dalam fungsi *view*, Django menggunakan ORM untuk mengambil data dari database (seperti `Certification.objects.all()`). Data yang diambil ini kemudian diserahkan ke fungsi `serializers.serialize()` untuk diubah menjadi format JSON. Terakhir, *view* mengembalikan data JSON tersebut menggunakan `HttpResponse` dengan *content type* `application/json` agar dapat ditampilkan di browser.

Kita wajib melakukan *serialization* karena data yang diambil dari *database* Django hanya berupa objek *class* Python yang kompleks saja. Web browser, JavaScript, atau aplikasi eksternal tidak mengerti cara membaca objek memori Python tersebut. *Serialization* berfungsi menerjemahkan objek Python yang terlihat rumit itu itu menjadi format teks standar (JSON) agar bisa dikirim melalui protokol HTTP dan dipahami oleh berbagai sistem di luar Django.

---

## AI Disclosure & Log Prompting
Dalam pengembangan tugas 3 ini, saya kembali menggunakan asisten AI sebagai partner diskusi teknis, khususnya untuk memperbaiki *bug* visual pada antarmuka dan *error* pada logika *backend*.

*   **Tools yang Digunakan:** Gemini 3.1 Pro
*   **Strategi Prompting:** Saya mengarahkan AI untuk fokus pada penyelesaian masalah (*troubleshooting*) dengan membagikan pesan *error* dari *browser*, potongan kode HTML/CSS, dan struktur URL yang saya miliki. Saya tidak meminta kode instan dari nol, melainkan meminta AI menganalisis di mana letak kesalahan sintaks pada fitur yang sedang saya kembangkan.
*   **Bagian Spesifik yang Dibantu AI:**
    *   Mendiagnosis dan merapikan struktur tombol *Action* (Edit dan Delete) yang bertumpuk akibat kesalahan struktur `<div>` di *flexbox*.
    *   Memecahkan *error* `TypeError: cannot unpack non-iterable UUID object` saat fitur Edit diklik dengan menambahkan parameter `pk=` pada pemanggilan ORM Django.
    *   Menyelaraskan nama *class* CSS (karena *underscore* nya ada yang single dan ada yang double dari tutorial 3) yang menyebabkan pop-up *modal* untuk menghapus tidak terkena-*styling*.
    *   Mencari solusi untuk merender gambar berukuran besar (17MB) yang gagal dimuat oleh API Google Drive dengan memanfaatkan *raw URL* dari GitHub.
*   **Analisis Kritis Keterbatasan AI & Perbaikan Manual:** 
    AI sangat cepat dalam menemukan kesalahan sintaks (seperti lupa menaruh `pk=` saat *query* UUID). Namun, dalam hal *image hosting*, AI awalnya berasumsi bahwa *link* gambar Google Drive saya untuk memberi thumbnail salah satu *certificate* salah atau karena tidak berakhiran ekstensi `.jpg`. AI memberikan saran standar untuk menggunakan platform eksternal seperti Postimages. Setelah saya menganalisis ulang situasinya dan menyadari masalah bukan pada URL melainkan pada ukuran *file* lokal `sertif-ddp0.jpg` yang mencapai 17.3MB, saya mencoba mengambil alih diskusi saya dengan AI tersebut. Saya secara proaktif mencoba memberi ide untuk mengunggah gambar tersebut ke GitHub dan meminta AI untuk mengonfirmasi cara mendapatkan *raw link* dari githubnya. Saya kemudian memutuskan secara manual untuk menghapus file lokal berukuran masif tersebut dari repositori demi menjaga efisiensi *storage*.
*   **Log Prompting:**
    *   *Prompt 1:* "wait kok jadinya malah gini ya? [Melampirkan *screenshot* dua tombol Hapus Sertifikasi yang tata letaknya berantakan serta potongan kode HTML]"
        *   *Respons AI:* AI mendeteksi adanya tag `<p>` berlebih di dalam *include modal* dan adanya pemisahan *container* `<div class="project-actions">` yang menyebabkan CSS *flexbox* gagal merender tombol secara sejajar.
    *   *Prompt 2:* "Kenapa pas gw pengen hapus sertifikasi jadinya kek gini? Tampilan UI nya emang jelek ya? TErus pas gw klik edit di salah satu certifications malah begini keluarnya, what happened? [Melampirkan *screenshot error TypeError* dan *modal popover* yang desainnya hilang]"
        *   *Respons AI:* AI memecah masalah menjadi dua. Pertama, AI menemukan bahwa atribut pencarian UUID di `get_object_or_404` kekurangan argumen `pk=`. Kedua, AI menyadari adanya ketidakcocokan penulisan nama *class* BEM CSS, di mana template saya menggunakan `_content` sedangkan CSS diatur menggunakan `__content` (dua *underscore*), sehingga *styling modal* tidak terbaca.
    *   *Prompt 3:* "tetep gabisa cok, ini keknya ada yang harus gw migrate modelnya ya buat masukin ke thumbnail? ... Ini buat thumbnailnya https://drive.google.com/thumbnail?id=..."
        *   *Respons AI:* AI mendiagnosis respons API dari *browser* dan menemukan bahwa ukuran gambar sertifikat asli saya terlalu besar sehingga server pembuat *thumbnail* Google Drive mengalami kegagalan proses. AI kemudian mengarahkan metode pengambilan tautan *raw image* langsung dari *repository* GitHub sebagai solusi yang lebih oke.

# Tugas 4
Maaf kak ke skip bikin AI disclosure nya :v

# Tugas 5
## Jawaban Pertanyaan Reflektif

### 1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!
*Debouncing* adalah teknik pemrograman yang digunakan untuk menunda eksekusi sebuah fungsi sampai pengguna berhenti melakukan aksi (for example: mengetik) selama durasi waktu tertentu. Pada fitur pencarian AJAX, teknik ini sangat penting karena mencegah aplikasi mengirim *request* HTTP ke server pada setiap huruf yang diketik. Tanpa *debouncing*, jika kita mengetik 10 huruf secara cepat, akan ada 10 *request* yang dikirim hampir bersamaan, yang mana bisa membebani kinerja server dan membuat antarmuka web menjadi lebih lambat.

### 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi `await` digunakan untuk menunda eksekusi baris kode selanjutnya sampai proses *asynchronous* (seperti mengambil data dari server menggunakan `fetch()`) benar-benar selesai dan menghasilkan *response*. Jika kita tidak menggunakan `await`, JavaScript tidak akan menunggu server membalas, melainkan langsung mengeksekusi kode di bawahnya. Akibatnya, saat kode mencoba memproses atau menampilkan data (misalnya dengan `.json()`), datanya masih berstatus *pending* atau kosong (*undefined*), yang akan menyebabkan *error* pada aplikasi sehingga UI gagal memuat daftar portofolio yang diinginkan.

### 3. Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!
Serangan XSS adalah kerentanan sistem keamanan di mana penyerang dapat menyisipkan script (seperti tag `<script>` atau `<img>` berbahaya) ke dalam situs web, yang kemudian dieksekusi oleh *browser* pengunjung lain. Data yang dirender menggunakan AJAX/JavaScript (seperti mengubah `.innerHTML`) lebih rentan karena *browser* akan langsung membaca dan mengeksekusi tag HTML mentah yang ada di dalam *string* tersebut tanpa difilter terlebih dahulu. Berbeda dengan template bawaan Django, di mana setiap variabel yang diapit `{{ }}` secara otomatis sudah di-*escape* (diubah menjadi sebuah entity yg aman seperti `&lt;` dan `&gt;`) sebelum dikirim ke *browser*, sehingga mematikan fungsi skrip jahat tersebut.

---

## AI Disclosure & Log Prompting

Dalam pengembangan tugas 5 ini, saya kembali menggunakan asisten AI sebagai partner diskusi teknis, khususnya untuk mentransisi aplikasi dari rendering sisi server menjadi aplikasi berbasis AJAX, serta mengimplementasikan keamanan Anti-XSS.

*   **Tools yang Digunakan:** Gemini 3.1 Pro
*   **Strategi Prompting:** Saya memberikan instruksi bertahap terkait implementasi AJAX, serta memberikan potongan kode seperti fungsi JavaScript yang *error*, *file* `views.py`, dan melampirkan *screenshot DevTools Browser* saat terjadi *bug* pada antarmuka. Saya menggunakan AI untuk mendiagnosis kendala spesifik dan sebagai teman *brainstorming* dibandingkan memintanya membuat seluruh aplikasi dari nol.
*   **Bagian Spesifik yang Dibantu AI:**
    *   Mendiagnosis masalah *file* CSS yang tidak terbaca dengan panduan inspeksi melalui tab *Network* dan penanganan *cache browser*.
    *   Memberikan simulasi cara menyuntikkan *payload* `<img src="x" onerror="alert('XSS!')">` ke dalam form untuk menguji celah keamanan secara lokal.
    *   Mengonfirmasi dan merapikan logika validasi hak akses (*superuser* dan *editor*) pada *views* saat mengimplementasikan CRUD dengan AJAX.
*   **Analisis Kritis Keterbatasan AI & Perbaikan Manual:** 
    Terkadang AI mengalami "halusinasi konteks" dengan memberikan referensi variabel JavaScript yang mengacu pada model *default* tutorial (menggunakan variabel seperti `project.tech_stack` atau `project.project_image_url`) yang tidak ada di struktur *database* saya. Akibatnya, aplikasi sempat gagal merender data. Sebagai perbaikan manual, saya secara mandiri harus menelusuri ulang baris kode JavaScript tersebut dan memetakan variabelnya agar sesuai dengan model saya sendiri (seperti mengubah target data ke `issuer`, `thumbnail`, dan memperbaiki variabel pelemparan UUID).
*   **Log Prompting:**
    *   *Prompt 1:* "Wait, kok pas gw buka localhost malah kek gini ya? gw baru buka web nya loh ya [Melampirkan *screenshot* portofolio nya hanya HTML mentah tanpa CSS]"
        *   *Respons AI:* AI mendiagnosis bahwa *browser* menahan file statis di *cache*. AI menyarankan langkah pengecekan mulai dari *hard refresh* (Ctrl+F5) dan membimbing saya menginspeksi tab *Network* pada *DevTools* untuk melacak status pemuatan file statis.
    *   *Prompt 2:* "Gw udah bikin buat di bagian show_experience di views.py, saya masih harus nambahin yang kayak di show_certifications kan ya soal title_query sama is_editor nya, untuk misahin apa yg bisa dilakuin semisal yg login itu editor"
        *   *Respons AI:* AI menyetujui analisis saya dan memvalidasi bahwa pengecekan `is_editor` memang krusial untuk menjaga konsistensi hak akses dari tugas sebelumnya. 
    *   *Prompt 3:* "Oke kalo begitu, gw gak perlu buat ngerjain yg bagian pendidikan ya? Karena kayak aneh gak sih pendidikan bisa ditambah dan diedit gitu wkwkw, itu biarin jadi data yang statis aja di bagian main ya?"
        *   *Respons AI:* AI setuju dengan keputusan desain tersebut, mengonfirmasi bahwa tidak semua modul di dalam *website* harus dinamis. AI mendukung pendekatan saya untuk mempertahankan bagian pendidikan sebagai data statis dan memfokuskan penerapan AJAX pada modul *Experience* secara lebih matang.

# Tugas 6
## Jawaban Pertanyaan Reflektif

### 1. Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan PUT dan PATCH beserta contoh kapan masing-masing sebaiknya digunakan!
*REST (Representational State Transfer)* adalah gaya arsitektur perancangan web API yang memperlakukan data sebagai *resource* yang dapat diakses melalui URI/endpoint unik, serta memanfaatkan *HTTP methods* standar (GET, POST, PUT, PATCH, DELETE) untuk menyatakan tindakan yang dilakukan terhadap *resource* tersebut. Mengembalikan data dalam format JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful karena JSON hanyalah format representasi data atau muatan payload saja. Suatu API baru dapat dikatakan RESTful jika mematuhi prinsip-prinsip arsitektur REST, di antaranya: URL murni menunjuk ke *resource* kata benda (misalnya `/api/v1/certifications/`) bukan kata kerja aksi (seperti `/api/add-certification/`), tindakan didefinisikan oleh *HTTP method*, pertukaran data bersifat *stateless*, serta memanfaatkan *HTTP status code* yang tepat untuk merepresentasikan hasil pemrosesan.

Perbedaan utama antara PUT dan PATCH terletak pada cakupan modifikasi datanya:
*   **PUT** bersifat sebagai penggantian representasi *resource* secara menyeluruh (*full replacement*). Klien wajib mengirimkan seluruh atribut atau *field* wajib dari objek tersebut. Jika ada *field* wajib yang tidak dikirim, server akan menolak permintaan dengan *error*. Contoh penggunaannya adalah ketika pengguna memperbarui seluruh informasi sertifikasi melalui formulir edit lengkap yang mencakup `title`, `issuer`, `date_issued`, `description`, dan `thumbnail` sekaligus.
*   **PATCH** bersifat sebagai pembaruan parsial (*partial update*). Klien hanya perlu mengirimkan *field* spesifik yang ingin diubah tanpa mempengaruhi nilai *field* lainnya yang tidak disertakan dalam *payload*. Contoh penggunaannya adalah ketika pengguna hanya ingin mengganti judul (*title*) atau URL gambar (*thumbnail*) sertifikasi melalui fitur edit cepat tanpa harus menyertakan kembali teks deskripsi atau tanggal terbitnya.

### 2. Jelaskan peran serializer pada Django REST Framework! Apa keuntungannya dibandingkan merakit dictionary secara manual dengan JsonResponse seperti pada Tutorial 05?
Peran *serializer* pada Django REST Framework adalah sebagai *two-way converter* antara data kompleks Django (seperti objek Model atau QuerySet) dengan format data primitif Python yang siap dirender menjadi JSON (proses serialisasi), serta mengubah *payload* JSON yang dikirimkan klien menjadi data Python tervalidasi yang siap disimpan ke *database* melalui ORM (proses deserialisasi).

Keuntungannya dibandingkan merakit *dictionary* secara manual dengan `JsonResponse`:
*   **Validasinya Terpusat dan Deklaratif:** *Serializer* menangani validasi tipe data, format URL, batasan panjang karakter, hingga pembersihan tag HTML (`strip_tags`) secara otomatis dan terpusat melalui method `validate_<field>`, menghasilkan respon *error* `400 Bad Request` yang konsisten dengan rincian *error* per *field*.
*   **Mendukung Operasi CRUD Bawaan:** Melalui `ModelSerializer`, method `.create()` dan `.update()` sudah terintegrasi langsung dengan model tanpa perlu menulis logika penyimpanan manual *field* demi *field*.
*   **Kode Lebih Bersih dan Aman:** Menghilangkan perulangan manual (`for loop`) untuk merakit *dictionary* satu per satu, mendukung kalkulasi *field* dinamis melalui `SerializerMethodField` (seperti `star_count` dan status relasi `is_starred`), serta mencegah kebocoran data sensitif karena *field* yang diekspos ditentukan secara eksplisit.

### 3. Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan permission class di server, bukan hanya dengan menyembunyikan tombol di template?
*Autentikasi (Authentication)* adalah proses untuk memverifikasi identitas pengguna yang menjawab pertanyaan *"Siapa Anda?"* (misalnya mengenali akun melalui *session cookie* dan mengisi objek `request.user`). Sedangkan *autorisasi (Authorization)* adalah proses penentuan hak akses yang menjawab pertanyaan *"Apa yang boleh Anda lakukan?"*, yaitu memutuskan apakah akun yang sudah teridentifikasi berhak menjalankan suatu tindakan terhadap *resource* tertentu (misalnya membedakan hak akses antara *superuser*, *editor*, dan pengunjung biasa).

Pemeriksaan hak akses ini mutlak harus dilakukan menggunakan `permission_classes` di sisi server karena menyembunyikan tombol di *template* HTML hanyalah aspek kenyamanan antarmuka pengguna (UI/UX) dan tidak memberikan perlindungan keamanan nyata (*security through obscurity*). Pengguna mana pun dapat dengan mudah mem-*bypass* antarmuka web dan mengirimkan permintaan mutasi data secara langsung ke URL endpoint (misalnya menggunakan Fetch API di Console browser, cURL, atau Postman). Jika server tidak memvalidasi hak akses melalui *permission class*, aksi manipulasi data yang tidak sah tersebut akan tetap dieksekusi oleh *database* kita.

### 4. Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai SessionAuthentication! Mengapa test yang memakai force_authenticate tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?
Permintaan yang mengubah data tetap memerlukan token CSRF karena `SessionAuthentication` mengandalkan *cookie browser* (`sessionid`) untuk mengenali pengguna yang login. Mengingat *browser* secara otomatis menyertakan *cookie* tersebut pada setiap *request* yang dikirimkan ke domain yang sama (bahkan jika *request* tersebut dipicu oleh pihak ketiga), aplikasi rentan terhadap serangan Cross-Site Request Forgery (CSRF). Penyerang dapat menjebak pengguna yang sedang dalam sesi aktif untuk mengeksekusi *request* mutasi (POST, PUT, PATCH, DELETE) tanpa disadari. Header `X-CSRFToken` diperlukan karena token ini hanya bisa dibaca oleh skrip yang berada pada *origin* yang sama (*Same-Origin Policy*), sehingga server dapat memastikan permintaan benar-benar berasal dari interaksi sah pengguna di website portofolio.

Pengujian yang hanya memakai `force_authenticate` tidak cukup untuk membuktikan perlindungan CSRF karena method tersebut sengaja memotong (*bypass*) alur autentikasi bawaan Django dan langsung menempelkan objek `request.user` ke *request* tanpa melalui proses login nyata ataupun pemeriksaan *middleware* CSRF. Akibatnya, *request* akan selalu dianggap lolos meskipun tanpa token CSRF. Untuk membuktikan bahwa pertahanan CSRF benar-benar aktif menolak *request* ilegal, pengujian harus menggunakan `APIClient(enforce_csrf_checks=True)` yang digabungkan dengan autentikasi berbasis sesi sungguhan melalui `.login()`.

---

## AI Disclosure & Log Prompting
Dalam pengembangan Tugas 6 ini, saya menggunakan asisten AI sebagai rekan diskusi teknis dan pemecahan masalah, terutama dalam membantu penyesuaian integrasi JavaScript pada frontend serta penelusuran kegagalan unit test.

*   **Tools yang Digunakan:** Gemini 3.1 Pro
*   **Strategi Prompting:** Saya mengarahkan AI untuk fokus pada penyelesaian *bug* dan implementasi fitur spesifik, seperti menanyakan alur pengiriman request asinkronus pada form modal dan melampirkan pesan *error* terminal saat pengujian test suite.
*   **Bagian Spesifik yang Dibantu AI:**
    *   Membantu menyusun skrip JavaScript pada antarmuka frontend untuk menangani pengiriman data dari form modal edit secara asinkronus (`PATCH`) menggunakan Fetch API.
    *   Membantu menelusuri akar penyebab kegagalan pada 4 unit test lama di `main/tests.py` yang terpengaruh oleh transisi rendering halaman ke AJAX.
*   **Analisis Kritis Keterbatasan AI & Perbaikan Manual:** 
    AI sempat memberikan saran template skrip JavaScript yang mengasumsikan penamaan elemen DOM default tutorial, sehingga beberapa fungsi sempat tidak merespons. Sebagai perbaikan manual, saya meninjau kembali kode tersebut dan menyesuaikan ID elemen form, penamaan field payload, serta alur pengisian nilainya agar selaras dengan template sertifikasi saya. Selain itu, pada bagian unit test, saya secara mandiri menyesuaikan *assertion* agar tetap memverifikasi kerangka DOM HTML sekaligus memastikan integritas data melalui pemanggilan endpoint API yang relevan.
*   **Log Prompting:**
    *   *Prompt 1:* "Gimana cara bikin script JavaScript buat modal edit sertifikasi ini biar bisa kirim PATCH lewat fetch ke endpoint API tanpa harus ngereload halaman?"
        *   *Respons AI:* AI memberikan contoh penanganan event submit pada form modal edit menggunakan method `PATCH`, lengkap dengan pembacaan token CSRF dan pengiriman payload dalam format JSON.
    *   *Prompt 2:* "Test yang di tests.py kok ada 4 yang fail pas di-run ya, padahal yang tests_api lolos semua? [Melampirkan screenshot terminal FAILED (failures=4)]"
        *   *Respons AI:* AI menjelaskan bahwa test lama gagal karena masih memeriksa keberadaan string data langsung pada respons HTML mentah, padahal data sekarang dimuat secara dinamis via AJAX, lalu memberikan saran penyesuaian assertion-nya.