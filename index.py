import pytesseract
from PIL import Image

# Atur path ke binary Tesseract OCR di Ubuntu
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Buka gambar
img = Image.open("012152400_1601901778-kata1.jpg")

# Ekstrak teks dari gambar
text = pytesseract.image_to_string(img)

# Tampilkan hasil ekstraksi teks
print(text)