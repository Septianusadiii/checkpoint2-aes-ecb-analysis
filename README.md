# Checkpoint 2 — AES-ECB Security Analysis

Proyek tugas Kriptografi **Checkpoint 2: Buktikan atau Bantah**. Kode dikembangkan dari praktikum Minggu 4: **4A Demo Konsep ECB Leakage**, **4B AES-ECB asli**, dan **4C ECB vs CBC**.

## Tujuan
Menguji klaim: **"Selama sebuah data sudah dienkripsi dengan AES, semua informasi termasuk polanya pasti tersembunyi."** Eksperimen menunjukkan bahwa klaim ini **tidak selalu benar**, karena mode ECB membocorkan kesamaan blok plaintext yang berulang.

## Isi proyek
- `checkpoint2.py` — satu file Python untuk eksperimen.
- `ANALISIS_CP2.md` — tulisan analisis bukti eksperimen.
- `POSTINGAN_LINKEDIN.md` — draft singkat untuk publikasi LinkedIn.

## Cara menjalankan di VS Code
1. Buka folder proyek di Visual Studio Code.
2. Pastikan ekstensi Python dan Python 3 tersedia.
3. **Sekali saja**, install library asli praktikum melalui terminal **di dalam VS Code**:

   ```shell
   py -m pip install pycryptodome
   ```

   Jika `py` tidak dikenali, gunakan `python -m pip install pycryptodome`.
4. Buka `checkpoint2.py`, lalu klik **Run Python File** di kanan atas.
5. Amati keluaran bagian `[2]` sampai `[5]` pada panel terminal VS Code.

## Bukti yang dicari
- Dua blok plaintext 16 byte identik.
- Dua blok ciphertext pertama AES-ECB **sama** (`True`).
- Dua blok ciphertext pertama AES-CBC pada pengujian **berbeda** (`False`).
- Dekripsi keduanya berhasil mengembalikan plaintext (`True`).

**Catatan:** Nilai IV dan ciphertext CBC berubah pada tiap eksekusi, karena IV dibuat secara acak. Padding menambahkan satu blok ciphertext sehingga totalnya tiga blok. Kunci dalam kode hanya untuk demo, jangan digunakan dalam sistem nyata.

## Kesimpulan
ECB tidak memberikan kerahasiaan pola antarblok yang identik. CBC menggunakan IV dan chaining sehingga menghilangkan kebocoran kesamaan blok langsung dalam contoh, tetapi CBC tidak menyediakan autentikasi. Aplikasi baru sebaiknya menggunakan enkripsi terautentikasi seperti AES-GCM.

## Dokumentasi screenshot
1. Kode bagian `AES.MODE_ECB` dan perbandingan blok ECB.
2. Kode bagian `AES.MODE_CBC` beserta IV acak.
3. Output terminal `[3]`, `[4]`, dan `[5]`.

Untuk keperluan pembelajaran, bukan penyimpanan data penting.
