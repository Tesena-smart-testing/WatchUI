import cv2
import pytesseract



def image_to_text():
    '''
    PSM = Page Segmentation Mode
        - 0 = Orientation and script detection (OSD) only.
        - 1 = Automatic page segmentation with OSD.
        - 2 = Automatic page segmentation, but no OSD, or OCR. (not implemented)
        - 3 = Fully automatic page segmentation, but no OSD. (Default)
        - 4 = Assume a single column of text of variable sizes.
        - 5 = Assume a single uniform block of vertically aligned text.
        - 6 = Assume a single uniform block of text. (Default)
        - 7 = Treat the image as a single text line.
        - 8 = Treat the image as a single word.
        - 9 = Treat the image as a single word in a circle.
        - 10 = Treat the image as a single character.
        - 11 = Sparse text. Find as much text as possible in no particular order.
        - 12 = Sparse text with OSD.
        - 13 = Raw line. Treat the image as a single text line,
             bypassing hacks that are Tesseract-specific.

    OEM = Engine Mode
        - 0 = Original Tesseract only.
        - 1 = Neural nets LSTM only.
        - 2 = Tesseract + LSTM.
        - 3 = Default, based on what is available (Default)
    '''

    img_cv = cv2.imread(r'C:\development\scripty\WatchUI\Img\forpres.png')
    cv2.imshow('photo', img_cv)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img_rgb))

image_to_text()