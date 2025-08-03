# Kompres Gambar PRO

Aplikasi desktop untuk mengompresi gambar JPG/PNG dengan berbagai fitur yang memudahkan proses kompresi.

## Fitur Utama

- **Kompresi Gambar**: Mengurangi ukuran file gambar JPG/PNG tanpa kehilangan kualitas yang signifikan
- **Resize Gambar**: Mengubah ukuran gambar sesuai persentase yang diinginkan
- **Watermark**: Menambahkan teks watermark pada gambar
- **Konversi Format**: Mengonversi gambar PNG ke JPG
- **Penggabungan ke PDF**: Menggabungkan gambar ke dalam file PDF setelah kompresi
- **Pemrosesan Batch**: Memproses banyak gambar sekaligus dari folder

## Cara Penggunaan

1. **Pilih Gambar**:
   - Klik tombol "📁 Pilih Gambar" untuk memilih satu atau beberapa file gambar
   - Klik tombol "📂 Pilih Folder" untuk memproses semua gambar dalam folder

2. **Atur Pengaturan**:
   - Sesuaikan kualitas gambar menggunakan slider (10-100%)
   - Atur persentase resize gambar (10-100%)
   - Tambahkan teks watermark jika diperlukan
   - Centang opsi konversi PNG ke JPG jika ingin mengonversi
   - Centang opsi gabungkan ke PDF jika ingin membuat file PDF

3. **Kompresi Gambar**:
   - Klik tombol "🚀 Kompres Sekarang" untuk memulai proses kompresi
   - Hasil kompresi akan disimpan di folder yang sama dengan aplikasi

## Format yang Didukung

- JPG/JPEG
- PNG

## Persyaratan Sistem

- Sistem operasi Windows
- Python 3.6 atau lebih baru (jika menjalankan dari source code)
- Pustaka Python yang diperlukan:
  - customtkinter
  - Pillow
  - fpdf
  - PyPDF2

## Instalasi

1. Pastikan Python 3.6+ terinstal di sistem Anda
2. Instal pustaka yang diperlukan:
   ```
   pip install customtkinter Pillow fpdf PyPDF2
   ```
3. Jalankan aplikasi:
   ```
   python gambar-kompres.py
   ```

## File Hasil

Setelah proses kompresi selesai, aplikasi akan membuat file-file berikut:

- Gambar yang telah dikompresi (dengan nama yang sama)
- `hasil_kompres.txt`: Log proses kompresi
- `hasil_kompres.pdf`: File PDF gabungan (jika opsi dicentang)
- `hasil_kompres_compressed.pdf`: File PDF yang telah dikompresi

## Lisensi

Aplikasi ini dikembangkan oleh Habib Frambudi dan disediakan untuk penggunaan umum.
