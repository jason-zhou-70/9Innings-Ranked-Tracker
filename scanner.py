from PIL import Image
from pytesseract import pytesseract
import tesserocr

def main():
    # path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # image_path = r"C:\Users\Jason\Pictures\9Innings-Ranked-Pictures\IMG_1599_2.png"

    # img = Image.open(image_path)

    # pytesseract.tesseract_cmd = path_to_tesseract
    # text = pytesseract.image_to_string(img)
    # print(text)

    api = tesserocr.PyTessBaseAPI()
    img = Image.open(r'C:\Users\Jason\Pictures\9Innings-Ranked-Pictures\IMG_1599.png')
    api.SetImage(img)
    text = api.GetUTF8Text()
    print(text)
    print("satg")

if __name__ == "__main__":
    main()