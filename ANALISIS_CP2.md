# Laporan Analisis Checkpoint 2 — Buktikan atau Bantah

## 1. Klaim yang diuji
Klaim yang diuji adalah bahwa menggunakan algoritma AES saja sudah cukup untuk menyembunyikan setiap pola pada data. Pengujian dilakukan terhadap mode ECB menggunakan blok plaintext yang sama secara berulang. Sebagai pembanding, digunakan mode CBC dengan IV acak. Eksperimen dikembangkan dari kode praktikum Minggu 4 bagian 4A, 4B, dan 4C.

## 2. Metode percobaan
Pesan `AAAAAAAABBBBBBBBAAAAAAAABBBBBBBB` terdiri atas dua blok plaintext identik, masing-masing berukuran 16 byte. Pertama, program menampilkan demo sederhana yang membagi pesan menjadi blok empat karakter seperti Praktikum 4A. Berikutnya, data dienkripsi menggunakan AES-ECB dengan kunci contoh dari modul praktikum lalu diperiksa kesamaan dua blok ciphertext pertama. Setelah itu, pesan yang sama dienkripsi menggunakan AES-CBC dengan IV acak dan dibandingkan hasilnya.

## 3. Bukti yang diperoleh
Pada ECB, blok plaintext 1 dan 2 identik dan kedua blok ciphertext yang dihasilkan juga identik. Pada CBC, blok ciphertext 1 dan 2 berbeda meskipun kedua blok plaintext sama, karena setiap blok terhubung dengan hasil sebelumnya dan blok awal bergantung pada IV. Nilai ciphertext CBC berubah ketika IV baru digunakan saat program dijalankan kembali. Pengujian dekripsi mengonfirmasi bahwa kedua mode tetap mengembalikan pesan awal secara benar.

## 4. Analisis keamanan
Hasil ini **membantah** klaim bahwa menggunakan AES saja selalu cukup untuk menyembunyikan seluruh pola data. Kelemahan tersebut terkait **mode operasi ECB**, bukan bukti bahwa algoritma inti AES telah berhasil dipecahkan. Pengamat yang mengetahui bahwa dua blok ciphertext ECB sama dapat menyimpulkan bahwa kedua blok plaintext pada posisi tersebut juga sama jika kunci yang digunakan sama. CBC mengurangi kebocoran pola langsung ini tetapi tidak memberikan autentikasi atau jaminan bahwa ciphertext tidak dimodifikasi.

## 5. Kesimpulan
Eksperimen menunjukkan bahwa ECB membocorkan hubungan kesamaan antara blok plaintext yang berulang. CBC memperlihatkan hasil yang berbeda dalam kondisi pengujian yang sama karena penggunaan chaining dan IV. Oleh karena itu, memilih algoritma AES saja tidak cukup; pemilihan mode dan properti keamanan lain juga penting. Untuk aplikasi baru, enkripsi terautentikasi seperti AES-GCM merupakan pilihan yang lebih tepat daripada ECB atau CBC tanpa autentikasi.

## 6. Batasan
Pengujian hanya memeriksa kesamaan blok dan keberhasilan dekripsi pada satu pesan contoh, bukan serangan untuk memulihkan kunci AES. IV dan ciphertext CBC bersifat acak pada tiap eksekusi sehingga nilainya tidak selalu sama. Contoh menggunakan kunci tetap dari praktikum hanya untuk demonstrasi; jangan menggunakannya untuk aplikasi nyata.
