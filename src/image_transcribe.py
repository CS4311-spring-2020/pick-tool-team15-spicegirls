import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


class ImageTranscription:
    def ocr_core(fileName, directory):
        text = pytesseract.image_to_string(Image.open(directory + '/' + fileName))
        temp = directory + '/' + os.path.splitext(fileName)[0] + '.txt'
        file = open(temp, "w+")
        file.write(text)
        file.close()