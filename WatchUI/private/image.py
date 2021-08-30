'''Class representing the Image object.
'''
from skimage.metrics import structural_similarity
import cv2 as cv
import imutils
import time
import os

from WatchUI.common.types import CustomPath, ImageFormat
from WatchUI.interfaces.interface import Interface
from WatchUI.modules.reporting import Reporting


class Image(Interface, Reporting):
    def __init__(
        self,
        ssim_basic: float,
        format_image: ImageFormat,
        tesseract_path: CustomPath,
        outputs_folder: CustomPath,
        path_to_image_1: CustomPath,
        path_to_image_2: CustomPath,
    ) -> None:
        super().__init__(ssim_basic, format_image, tesseract_path, outputs_folder)
        self.path_to_image_1: CustomPath = path_to_image_1
        self.path_to_image_2: CustomPath = path_to_image_2

    def compare_images(self, path1, path2):
        self.img1 = cv.imread(path1, 1)
        self.img2 = cv.imread(path2, 1)

        # convert to grey
        gray_img1 = cv.cvtColor(self.img1, cv.COLOR_BGR2GRAY)
        gray_img2 = cv.cvtColor(self.img2, cv.COLOR_BGR2GRAY)

        # SSIM diff Img
        (self.score, diff) = structural_similarity(gray_img1, gray_img2, full=True)
        diff = (diff * 255).astype("uint8")

        # Threshold diff Img
        thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
        cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        self.cnts = imutils.grab_contours(cnts)

    def create_area(self, x1, y1, x2, y2,
                    save_folder,
                    image_format,
                    path_to_screen,
                    screen_name="screen"):
        self._check_dir(save_folder)
        save_folder = self.save_folder
        self._check_image_format(image_format)

        img = path_to_screen
        img_crop = cv.imread(img)
        crop_img = img_crop[
                   int(x1): int(y2), int(y1): int(x2)
                   ]  # Crop from {x, y, w, h } => {0, 0, 300, 400}
        if screen_name == "screen":
            cv.imwrite(save_folder + '/screen' + str(time.time()) + self.format, crop_img)
        else:
            cv.imwrite(save_folder + '/' + screen_name + self.format, crop_img)

    def rotate_image(self, path,
                     image_format,
                     save_folder,
                     rotate=0,
                     screen_name="rotate_screen",
                     ):
        self._check_dir(save_folder)
        save_folder = self.save_folder
        self._check_image_format(image_format)
        if os.path.exists(path):
            img = cv.imread(path)
            if int(rotate) == 0:
                rotate_image = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
                cv.imwrite(save_folder + '/' + screen_name + self.format, rotate_image)
            elif int(rotate) == 1:
                rotate_image = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
                cv.imwrite(save_folder + '/' + screen_name + self.format, rotate_image)
            elif int(rotate) == 2:
                rotate_image = cv.rotate(img, cv.ROTATE_180)
                cv.imwrite(save_folder + '/' + screen_name + self.format, rotate_image)
            else:
                raise AssertionError("You try to setup volume:" + str(rotate) +
                                     " which never exists. Please read documentations a try 0,1 or 2.")
        else:
            raise AssertionError("Path" + path + "doesnt exists")

    def create_area_from_image(self):
        pass

    def create_image_with_err(self):
        pass