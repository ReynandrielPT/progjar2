Server Waktu Berbasis TCP dengan Multithreading di Python
Repositori ini merupakan implementasi Server Waktu (Time Server) menggunakan bahasa pemrograman Python. Server dapat menerima banyak koneksi secara bersamaan (concurrent) menggunakan teknik multithreading, serta memproses perintah TIME dan QUIT dari klien menggunakan protokol TCP.

Informasi
Nama: Reynandriel Pramas Thandya

NRP: 5025231113

Mata Kuliah: Pemrograman Jaringan C

Deskripsi Umum
Server ini dibangun menggunakan pendekatan Object-Oriented Programming (OOP) dengan dua kelas utama:

Server: Mengelola socket server dan menerima koneksi dari klien.

ProcessTheClient: Menangani komunikasi dengan masing-masing klien dalam thread terpisah.

Server membuka koneksi pada IP 0.0.0.0 dan port 45000, dan hanya akan memproses request klien yang valid dengan format tertentu. Koneksi dari masing-masing klien ditangani secara paralel menggunakan thread baru.

Spesifikasi Teknis
Port dan Protokol
Port: 45000

Protokol Transport: TCP

Socket server dibuat menggunakan:

python
Copy
Edit
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
AF_INET: IPv4

SOCK_STREAM: TCP

Format Request
Server hanya akan memproses perintah yang memiliki format:

TIME\r\n: Mengembalikan waktu saat ini dalam format hh:mm:ss.

QUIT\r\n: Menutup koneksi dengan klien.

Perintah lainnya akan dianggap tidak valid dan direspon dengan Invalid command\r\n.

Format Response
Jika klien mengirimkan TIME\r\n, server akan merespon dengan:

nginx
Copy
Edit
JAM hh:mm:ss\r\n
Contoh:

nginx
Copy
Edit
JAM 13:27:45\r\n
Multithreading
Setiap koneksi klien ditangani oleh instance ProcessTheClient, yang merupakan turunan dari threading.Thread.

Thread baru dibuat setiap kali klien terhubung, sehingga server dapat menangani banyak permintaan secara bersamaan.

Struktur Program
bash
Copy
Edit
📦 root/
├── server_thread.py      # File utama berisi implementasi server dan multithreading
├── timeserver.py         # Contoh penggunaan server dan pengujian klien
└── README.md             # Dokumentasi proyek ini
server_thread.py
Berisi definisi dua kelas utama:

Server: Membuka socket, menerima koneksi, dan menginisiasi ProcessTheClient.

ProcessTheClient: Menerima, memfilter, dan merespons perintah dari klien.

timeserver.py
Contoh program klien yang dapat digunakan untuk menguji koneksi ke server dan mengirim perintah TIME atau QUIT.

Logging dan Penanganan Error
Setiap request yang diterima akan ditampilkan di terminal beserta alamat IP klien.

Jika terjadi exception saat pemrosesan, error akan ditampilkan.

Saat klien mengirim QUIT\r\n, koneksi akan ditutup secara teratur dengan logging.

Contoh Penggunaan
Menjalankan Server
bash
Copy
Edit
python server_thread.py
Contoh Output Server
pgsql
Copy
Edit
[INFO] Connection from 127.0.0.1:54012
[INFO] Received: TIME from 127.0.0.1
[INFO] Sent: JAM 14:53:22
[INFO] Connection from 127.0.0.1:54013
[INFO] Received: QUIT from 127.0.0.1
[INFO] Connection closed from 127.0.0.1
Contoh Output Klien
ruby
Copy
Edit
>> TIME
JAM 14:53:22

>> QUIT
Connection closed by server.
Pengujian
Pengujian dilakukan dengan:

Menjalankan server

Menghubungkan dua klien, masing-masing dengan 3 koneksi (total 6 thread klien)

Memastikan semua koneksi aktif, dapat mengirim TIME dan QUIT, serta diproses secara bersamaan oleh server

Hasil menunjukkan bahwa server membuat thread baru untuk setiap koneksi klien dan mampu menangani permintaan tanpa konflik atau blocking.

Ketergantungan
Python 3.x

Tidak menggunakan library eksternal (hanya socket, threading, dan datetime)

Kesimpulan
Server ini memenuhi seluruh spesifikasi soal:

Menggunakan TCP pada port 45000

Mendukung multithreading dan OOP

Memproses perintah TIME dan QUIT

Menangani banyak koneksi secara bersamaan

Lisensi
Repositori ini dibuat untuk keperluan akademik dalam mata kuliah Pemrograman Jaringan C di Institut Teknologi Sepuluh Nopember (ITS).

