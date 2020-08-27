import cv2
import pytesseract
from pdf2image import convert_from_path, convert_from_bytes
import tempfile


# Otestovat
def pdf_to_image(path_to_folder='', out_folder='/', first_page=None, last_page=None):
    with tempfile.TemporaryFile():
        convert_from_path(path_to_folder, output_folder=out_folder, first_page=first_page, last_page=last_page)
    return True


def rotate_image(path, rotate=0):
    img = cv2.imread(path)
    if int(rotate) == 0:
        rotate_image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    elif int(rotate) == 1:
        rotate_image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif int(rotate) == 3:
        rotate_image = cv2.rotate(img, cv2.ROTATE_180)
    else:
        print('Zadal jsi špatnou rotate value zadej mezi 0 3 ')
    cv2.imwrite('rotimg', rotate_image)


def show_text_in_img(path, show='N', tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
    '''
    Show img with box around text :-)

    '''
    oldImg = cv2.imread(path)

    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

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
    if show == 'N':
        cv2.imwrite('textIMG', img)
    else:
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.imwrite('textIMG', img)


def full_image_to_string(path, oem=3, psm=3, language='eng', tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
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
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    custom_oem_psm_config = r'--oem ' + oem + ' --psm ' + psm
    print(pytesseract.image_to_string(old_img, config=custom_oem_psm_config, lang=language))


def image_area_on_text(path, *coordinates, oem='3', psm='3', language='eng',tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
    string_list = []
    old_img = cv2.imread(path)
    len_coordinates = len(coordinates)
    if len_coordinates % 4 == 0:
        if len_coordinates / 4 == 1:
            crop_img = old_img[int(coordinates[1]): int(coordinates[3]), int(coordinates[0]): int(coordinates[2])]
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
            custom_oem_psm_config = r'--oem ' + oem + ' --psm ' + psm
            text = pytesseract.image_to_string(crop_img, config=custom_oem_psm_config, lang=language)
            return text
        else:
            num_coordinates = len_coordinates / 4
            a = 0
            i = 0
            while i < num_coordinates:
                x1 = coordinates[0 + a]
                y1 = coordinates[1 + a]
                x2 = coordinates[2 + a]
                y2 = coordinates[3 + a]
                crop_img = old_img[int(y1): int(y2), int(x1): int(x2)]
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                custom_oem_psm_config = r'--oem ' + oem + ' --psm ' + psm
                text = pytesseract.image_to_string(crop_img, config=custom_oem_psm_config, lang=language)
                string_list.append(text)
                i += 1
                a += 4
        return string_list
    else:
        print('špatně zadané souřadnice')


# show_text_in_img()


# full_image_to_string(r'C:\Users\honzik\PycharmProjects\WatchUI\Img\forpres.png')


image_area_on_text(r'C:\development\scripty\WatchUI\Img\forpres.png', 166, 133, 315, 175, 0, 0, 100, 100)
