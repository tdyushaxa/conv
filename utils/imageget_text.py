from pytesseract import image_to_string
from PIL import Image



def image_to_Text_async(path, lang):
    text = image_to_string(Image.open(path), lang=lang)
    return text
