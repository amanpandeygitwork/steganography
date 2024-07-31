from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open("new_decoded.png"))
print(text)
