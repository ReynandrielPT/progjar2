# TUGAS 2 PEMROGRAMAN JARINGAN C

### NRP

5025231113

### Nama

Reynandriel Pramas Thandya

---

## Deskripsi Umum

Buatlah sebuah program time server dengan ketentuan sebagai berikut:

* Membuka port di port 45000 dengan transport TCP
* Untuk memenuhi soal poin a, dapat digunakan kode atau program yang diberikan oleh soal poin b.

Kode program tersebut telah dapat membuka koneksi sebagai server dengan multithreading untuk menerima beberapa koneksi sekaligus. Program bekerja dengan bentuk **OOP (Object-Oriented Programming)** dengan dua class utama:

### Class `Server`

Memiliki atribut berupa:

* daftar client (array of client)
* socket
* thread (turunan dari `threading.Thread`)

Fungsi:

* `__init__()` untuk inisialisasi
* `run()` untuk membuka koneksi dan mendengar seluruh koneksi (binding ke `0.0.0.0:8889`, lalu listen, dan menerima koneksi baru)

Jika ada koneksi, `Server` akan membuat instance `ProcessTheClient` untuk memproses data.

### Class `ProcessTheClient`

Turunan dari `threading.Thread`, memiliki:

* atribut: connection, address (IP address client), thread
* fungsi `__init__()` untuk inisialisasi
* fungsi `run()` untuk memproses data (menerima data 32 byte dan mengirimkan kembali)

### Fungsi `main`

* Membuat objek `Server` dan menjalankannya sebagai thread
* Setiap koneksi klien akan ditangani oleh thread `ProcessTheClient`

## Modifikasi

### Port dan Transport

* Ubah port default dari 8889 menjadi 45000
* Transport sudah menggunakan TCP (indikasi: `AF_INET`, `SOCK_STREAM`)

### Multithreading

* Kelas `Server` dan `ProcessTheClient` merupakan turunan dari `thread.Thread`
* Setiap instance dijalankan sebagai thread baru

### Format Request

* Diawali dengan string `TIME` dan diakhiri dengan karakter `13` (`\r`) dan `10` (`\n`)
* Jika tidak sesuai, koneksi akan ditutup
* Jika sesuai, lakukan logging IP dan pesan dari klien
* Lakukan pengecekan apakah teks adalah `TIME` atau `QUIT`

### Penanganan `QUIT`

* Jika menerima `QUIT\r\n`, koneksi ditutup dan logging ditampilkan
* Gunakan blok `finally` untuk menutup koneksi
* Tambahkan logging jika terjadi exception

### Format Response

* Untuk `TIME\r\n`, respon: `JAM <hh:mm:ss>\r\n`
* Gunakan modul `datetime` dan fungsi `strftime("%H:%M:%S")`
* Gunakan `f-string` untuk membentuk string respon
* Ubah string ke bytes sebelum dikirim

### Penanganan Invalid Command

* Tambahkan blok `else` jika perintah tidak dikenali
* Kirim pesan `Invalid command\r\n` ke klien
* Tutup koneksi

## Pengujian

### Contoh Pengujian 1 Klien 3 Thread

* Server menerima koneksi dari satu klien yang membuat 3 koneksi (3 thread)
* Total thread: 1 (server) + 3 (klien)
* Output menunjukkan setiap permintaan `TIME` dan `QUIT` diproses secara paralel

### Contoh Pengujian 2 Klien 3 Thread Masing-masing

* Total thread: 1 (server) + 6 (2 klien \* 3 koneksi)
* Terlihat pada output bahwa semua thread aktif dan memproses permintaan klien secara bersamaan

## Kesimpulan

Program telah berhasil:

* Membuka koneksi TCP pada port 45000
* Menggunakan multithreading untuk menangani koneksi secara concurrent
* Memproses request sesuai format yang ditentukan (`TIME` dan `QUIT`)
* Memberikan respon dalam format string UTF-8 dan menangani kesalahan input
