import cv2
import pytesseract


def show_text_in_img(path):
    '''
    Show img with box around text :-)

    '''
    oldImg = cv2.imread(path)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    h, w, _ = oldImg.shape  # assumes color image

    # run tesseract, returning the bounding boxes
    boxes = pytesseract.image_to_boxes(oldImg)  # also include any config options you use

    img = oldImg
    # draw the bounding boxes on the image
    for b in boxes.splitlines():
        print(b)
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

    # show annotated image and wait for keypress
    cv2.imshow('img', img)
    cv2.waitKey(0)



def full_image_to_string(path, oem=3, psm=3):
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
    old_img = cv2.imread(path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    custom_oem_psm_config = r'--oem ' + oem + ' --psm ' + psm
    print(pytesseract.image_to_string(old_img, config=custom_oem_psm_config))


def image_area_to_string(path, x1, y1, x2, y2, oem='3', psm='3', language='eng+ces'):
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

    old_img = cv2.imread(path)
    crop_img = old_img[int(y1): int(y2), int(x1): int(x2)]
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    custom_oem_psm_config = r'--oem ' + oem + ' --psm ' + psm
    print(pytesseract.image_to_string(crop_img, config=custom_oem_psm_config, lang=language))


# show_text_in_img()


# full_image_to_string(r'C:\Users\honzik\PycharmProjects\WatchUI\Img\forpres.png')


image_area_to_string(r'C:\Users\honzik\PycharmProjects\WatchUI\Img\forpres.png', 166, 133, 315, 175)