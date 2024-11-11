
# JPG to PDF Converter & PDF Merger

## Fitur
- **Konversi JPG ke PDF**: Pilih beberapa file JPG dan konversikan masing-masing menjadi file PDF.
- **Menggabungkan PDF**: Pilih beberapa file PDF untuk digabungkan menjadi satu file PDF.


## Persyaratan Sistem
- Python 3.x
- Modul-modul Python berikut:
  - `tkinter` (sudah termasuk dalam instalasi Python)
  - `Pillow`
  - `PyPDF2`
  - `reportlab`

## Instalasi
1. Clone repositori ini ke lokal Anda:
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. Install dependensi dengan `pip`:
   ```bash
   pip install Pillow PyPDF2 reportlab
   ```

## Cara Menggunakan
1. Jalankan skrip Python:
   ```bash
   python jpg-convert.py
   ```

2. Gunakan tampilan GUI untuk:
   - Mengonversi file JPG ke PDF dengan tombol **"Convert JPG to PDF"**.
   - Menggabungkan beberapa file PDF dengan penambahan teks kustom di setiap halaman dengan tombol **"Merge PDFs & Add Title"**.

## Contoh
- Jika Anda ingin menggabungkan beberapa file PDF dan menambahkan teks **"Programed by Habib Frambudi"** di pojok kanan bawah setiap halaman, pilih file-file PDF yang ingin digabungkan, kemudian program akan membuat file PDF gabungan dengan teks tersebut.

## Struktur Proyek
- **jpg-convert.py**: Skrip utama untuk aplikasi GUI yang mengelola konversi JPG ke PDF dan penggabungan PDF.
  
## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini:
1. Fork repositori ini.
2. Buat branch baru untuk fitur Anda: `git checkout -b fitur-baru`.
3. Commit perubahan Anda: `git commit -m 'Menambahkan fitur baru'`.
4. Push ke branch: `git push origin fitur-baru`.
5. Buat pull request.

