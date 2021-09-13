from WatchUI.IBasics.Basics import Basics
import time
import cv2 as cv
from skimage.metrics import structural_similarity
import imutils

class Image(Basics):
    def __init__(self, outputs_folder, ssim_basic, format_image, tesseract_path):
        super().__init__(outputs_folder, ssim_basic, format_image, tesseract_path)
    def compare_images(
            self, path1, path2, save_folder, ssim, image_format
    ):
        """Comparing images

        It compares two images from the two paths and, if there are differences, saves the image with the errors highlighted
        in the folder: ../Save Image

        path1 = path to the first image to be compared
        path2 = path to the second image to be compared

        Example: Compare two image ../image1.png ../Image2.png
        """
        self.check_dir(save_folder)
        self.check_ssim(ssim)
        self.check_image_format(image_format)
        self.check_image_exists(path1)
        self.check_image_exists(path2)

        # Compare image
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

        # Create frame in diff area
        for c in self.cnts:
            (x, y, w, h) = cv.boundingRect(c)
            cv.rectangle(self.img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.rectangle(self.img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Show image

        if float(self.score) < self.ssim:
            self.robotlib.log_to_console(self.ssim)
            self.robotlib.log_to_console(self.score)
            cv.imwrite(
                self.save_folder + "/Img" + str(time.time()) + self.format, self.img2
            )
            self.robotlib.fail("*INFO* Save file with difference")
        else:
            img_diff = cv.hconcat([self.img1, self.img2])
            time_ = str(time.time())
            self.seleniumlib.capture_page_screenshot(
                save_folder + "/Img" + time_ + self.format
            )
            cv.imwrite(save_folder + "/Img" + time_ + self.format, img_diff)
            self.robotlib.log_to_console(
                "Image has diff: {} ".format(self.score)
            )
