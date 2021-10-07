from PIL import Image
import pytesseract

def recognize(image):
    im = Image.open(image)
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    text = pytesseract.image_to_string(im).strip()
    # print(pytesseract.image_to_string(im))
    print(text)
    return text
