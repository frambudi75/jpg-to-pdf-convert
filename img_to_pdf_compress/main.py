def main():
    import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
import PyPDF2

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ImageCompressorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Kompres Gambar PRO")
        self.geometry("800x750")
        self.resizable(False, False)

        self.image_paths = []
        self.output_folder = os.getcwd()

        self.label_title = ctk.CTkLabel(self, text="📷 Kompres Gambar JPG/PNG By:Habib Frambudi", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=10)

        self.file_frame = ctk.CTkFrame(self)
        self.file_frame.pack(pady=5)

        self.file_button = ctk.CTkButton(self.file_frame, text="📁 Pilih Gambar", command=self.select_files)
        self.file_button.grid(row=0, column=0, padx=10)

        self.folder_button = ctk.CTkButton(self.file_frame, text="📂 Pilih Folder", command=self.select_folder)
        self.folder_button.grid(row=0, column=1, padx=10)

        self.quality_slider = ctk.CTkSlider(self, from_=10, to=100, number_of_steps=18, command=self.update_quality_label)
        self.quality_slider.set(85)
        self.quality_slider.pack(pady=5)
        self.quality_label = ctk.CTkLabel(self, text="Kualitas: 85%")
        self.quality_label.pack()

        self.resize_slider = ctk.CTkSlider(self, from_=10, to=100, number_of_steps=18, command=self.update_resize_label)
        self.resize_slider.set(100)
        self.resize_slider.pack(pady=5)
        self.resize_label = ctk.CTkLabel(self, text="Resize: 100% (tidak diubah)")
        self.resize_label.pack()

        self.watermark_entry = ctk.CTkEntry(self, placeholder_text="Teks Watermark (opsional)")
        self.watermark_entry.pack(pady=5)

        self.png_convert_chk = ctk.CTkCheckBox(self, text="Konversi PNG ke JPG")
        self.png_convert_chk.pack(pady=2)

        self.convert_pdf_chk = ctk.CTkCheckBox(self, text="Gabungkan ke PDF setelah kompres")
        self.convert_pdf_chk.pack(pady=2)

        self.compress_button = ctk.CTkButton(self, text="🚀 Kompres Sekarang", command=self.compress_all)
        self.compress_button.pack(pady=10)

        self.output_text = ctk.CTkTextbox(self, height=200, width=750)
        self.output_text.pack(pady=10)

    def update_quality_label(self, value):
        self.quality_label.configure(text=f"Kualitas: {int(float(value))}%")

    def update_resize_label(self, value):
        val = int(float(value))
        text = "Resize: 100% (tidak diubah)" if val == 100 else f"Resize: {val}%"
        self.resize_label.configure(text=text)

    def select_files(self):
        paths = filedialog.askopenfilenames(title="Pilih gambar JPG/PNG", filetypes=[("Images", "*.jpg *.jpeg *.png")])
        if paths:
            self.image_paths = list(paths)
            self.output_text.insert("end", f"✅ {len(paths)} gambar dipilih.\n")

    def select_folder(self):
        folder_path = filedialog.askdirectory(title="Pilih Folder Gambar")
        if folder_path:
            self.image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
            self.output_text.insert("end", f"✅ {len(self.image_paths)} gambar dari folder dipilih.\n")

    def compress_all(self):
        if not self.image_paths:
            messagebox.showerror("Tidak ada file", "Silakan pilih gambar terlebih dahulu.")
            return

        quality = int(self.quality_slider.get())
        resize = int(self.resize_slider.get())
        watermark = self.watermark_entry.get()
        convert_png = self.png_convert_chk.get()
        to_pdf = self.convert_pdf_chk.get()

        total_saving = 0
        total_orig = 0
        total_comp = 0
        log = []
        compressed_paths = []

        for path in self.image_paths:
            try:
                orig_size = os.path.getsize(path)
                img = Image.open(path)

                if resize < 100:
                    w, h = img.size
                    img = img.resize((int(w * resize / 100), int(h * resize / 100)), Image.Resampling.LANCZOS)

                if watermark:
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.load_default()
                    draw.text((10, 10), watermark, font=font, fill=(255,255,255))

                ext = os.path.splitext(path)[1].lower()
                save_path = os.path.join(self.output_folder, os.path.basename(path))
                if convert_png and ext == ".png":
                    save_path = save_path.replace(".png", ".jpg")
                    img = img.convert("RGB")

                img.save(save_path, quality=quality, optimize=True)
                comp_size = os.path.getsize(save_path)

                saving = orig_size - comp_size
                total_saving += saving
                total_orig += orig_size
                total_comp += comp_size

                compressed_paths.append(save_path)

                log.append(f"{os.path.basename(path)}: {orig_size//1024}KB → {comp_size//1024}KB")
            except Exception as e:
                log.append(f"❌ Gagal: {os.path.basename(path)} - {e}")

        percent = int(100 * (total_orig - total_comp) / total_orig) if total_orig > 0 else 0
        log.append(f"\nTotal saving: {total_orig//1024}KB → {total_comp//1024}KB (↓{percent}%)")

        self.output_text.insert("end", "\n".join(log) + "\n")
        with open("hasil_kompres.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(log))

        if to_pdf and compressed_paths:
            try:
                pdf = FPDF(unit="pt")
                for img_path in compressed_paths:
                    img = Image.open(img_path)
                    img = img.convert("RGB")
                    w, h = img.size
                    orientation = 'L' if w > h else 'P'
                    pdf.add_page(orientation=orientation, format=(w, h))
                    pdf.image(img_path, x=0, y=0, w=w, h=h)
                pdf_path = os.path.join(self.output_folder, "hasil_kompres.pdf")
                pdf.output(pdf_path)
                
                # Kompresi PDF menggunakan PyPDF2
                compressed_pdf_path = os.path.join(self.output_folder, "hasil_kompres_compressed.pdf")
                self.compress_pdf(pdf_path, compressed_pdf_path)
                
                self.output_text.insert("end", f"\n📄 PDF disimpan: {pdf_path}\n")
                self.output_text.insert("end", f"\n📄 PDF terkompresi disimpan: {compressed_pdf_path}\n")
            except Exception as e:
                self.output_text.insert("end", f"❌ Gagal membuat PDF: {e}\n")

        messagebox.showinfo("Selesai", f"Kompresi selesai! Total penghematan: {percent}%")

    def compress_pdf(self, input_path, output_path):
        """Kompresi file PDF menggunakan PyPDF2"""
        try:
            with open(input_path, 'rb') as input_file:
                reader = PyPDF2.PdfReader(input_file)
                writer = PyPDF2.PdfWriter()
                
                for page in reader.pages:
                    writer.add_page(page)
                
                # Menulis file PDF yang dikompresi
                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)
        except Exception as e:
            print(f"Error saat mengompresi PDF: {e}")

if __name__ == "__main__":
    app = ImageCompressorApp()
    app.mainloop()

    print("Tool konversi JPG ke PDF jalan!")
