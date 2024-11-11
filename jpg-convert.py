import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from PyPDF2 import PdfMerger

class PDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JPG to PDF Converter & PDF Merger")
        self.root.geometry("400x200")
        
        # Title label
        self.title_label = tk.Label(root, text="JPG to PDF & PDF Merger", font=("Helvetica", 14))
        self.title_label.pack(pady=10)

        # Button to convert JPG to PDF
        self.jpg_to_pdf_button = tk.Button(root, text="Convert JPG to PDF", command=self.convert_jpg_to_pdf)
        self.jpg_to_pdf_button.pack(pady=10)

        # Button to merge PDFs
        self.merge_pdf_button = tk.Button(root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_pdf_button.pack(pady=10)

        # Title label
        self.title_label = tk.Label(root, text="By Habib Frambudi", font=("Helvetica", 8))
        self.title_label.pack(pady=10)


    def convert_jpg_to_pdf(self):
        # Ask for JPG file(s)
        jpg_files = filedialog.askopenfilenames(title="Select JPG Files", filetypes=[("JPG Files", "*.jpg")])
        if not jpg_files:
            return
        
        for jpg_file in jpg_files:
            # Convert each JPG to PDF
            try:
                image = Image.open(jpg_file)
                pdf_file = jpg_file.rsplit(".", 1)[0] + ".pdf"
                image.save(pdf_file, "PDF", resolution=100.0)
                messagebox.showinfo("Success", f"File converted to {pdf_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to convert {jpg_file}. Error: {str(e)}")

    def merge_pdfs(self):
        # Ask for PDF file(s)
        pdf_files = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")])
        if not pdf_files:
            return

        # Ask for output PDF file
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not output_file:
            return
        
        # Merge PDFs
        merger = PdfMerger()
        try:
            for pdf in pdf_files:
                merger.append(pdf)
            merger.write(output_file)
            merger.close()
            messagebox.showinfo("Success", f"PDFs merged into {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs. Error: {str(e)}")


# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFConverterApp(root)
    root.mainloop()
