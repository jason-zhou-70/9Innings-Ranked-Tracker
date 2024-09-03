from PIL import Image
import cv2
import tesserocr
import pytesseract

def main():
    # image = cv2.imread('/home/jason/Pictures/9Innings-Ranked-Pictures/test_cropped.png', cv2.IMREAD_GRAYSCALE)
    # binary_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    # img = Image.fromarray(binary_image)
    # api = tesserocr.PyTessBaseAPI()
    # api.SetImage(img)
    # text = api.GetUTF8Text()
    # print(text)
    
    img = cv2.imread('/home/jason/Pictures/9Innings-Ranked-Pictures/test_cropped.png', cv2.IMREAD_GRAYSCALE)
    thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    thresh = cv2.resize(thresh, (0,0), fx = 2, fy = 1.5)
    
    text = pytesseract.image_to_string(thresh, config='--psm 6')
    print(text)

if __name__ == "__main__":
    main()