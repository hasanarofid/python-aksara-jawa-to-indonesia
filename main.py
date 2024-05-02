import tkinter as tk
from tkinter import Frame, Button, Text, Label, Scrollbar, filedialog
from PIL import Image, ImageTk
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Konversi Teks dari Gambar")
        self.geometry("600x400")
        
        self.img_label = Label(self, text="Gambar akan ditampilkan di sini")
        self.img_label.pack(pady=10)

        self.upload_button = Button(self, text="Unggah Gambar", command=self.upload_image)
        self.upload_button.pack(pady=5)

        self.result_text = Text(self, height=10, width=50)
        self.result_text.pack(pady=10)
        
    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img.thumbnail((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            self.img_label.config(image=img_tk)
            self.img_label.image = img_tk
            text = self.extract_text(img)
            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", text)

    def extract_text(self, img):
        # Simpan gambar ke file sementara
        img_path = "temp_image.png"
        img.save(img_path)

        # Ekstrak teks dari gambar sementara
        text = pytesseract.image_to_string(img_path)

        # Hapus file sementara setelah ekstraksi teks selesai
        os.remove(img_path)

        return text

app = App()
app.mainloop()