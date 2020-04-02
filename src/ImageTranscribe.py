try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

print(ocr_core('/Users/dima/Desktop/pick-tool-team15-spicegirls/Resources/pic.png'))