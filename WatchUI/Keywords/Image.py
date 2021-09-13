from WatchUI.IBasics.Basics import Basics
import time
import cv2 as cv
from skimage.metrics import structural_similarity
import imutils


class Image(Basics):
    save_folder_path = "../Outputs"
    starts_ssim = 1.0
    starts_format_image = "png"

    def compare_images(
            self, path1, path2, save_folder=save_folder_path, ssim=starts_ssim, image_format=starts_format_image
    ):
        """Comparing images

        It compares two images from the two paths and, if there are differences, saves the image with the errors highlighted
        in the folder: ../Save Image

        path1 = path to the first image to be compared
        path2 = path to the second image to be compared

        Example: Compare two image ../image1.png ../Image2.png
        """
        save_folder = self.check_dir(save_folder)
        ssim = self.check_ssim(ssim)
        img_format = self.check_image_format(image_format)
        self.check_image_exists(path1)
        self.check_image_exists(path2)

        # Compare image
        img1 = cv.imread(path1, 1)
        img2 = cv.imread(path2, 1)

        # convert to grey
        gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        # SSIM diff Img
        (score, diff) = structural_similarity(gray_img1, gray_img2, full=True)
        diff = (diff * 255).astype("uint8")

        # Threshold diff Img
        thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
        cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # Create frame in diff area
        for c in cnts:
            (x, y, w, h) = cv.boundingRect(c)
            cv.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)


        print(save_folder)
        # Show image
        if float(score) < ssim:
            cv.imwrite(
                save_folder + "/Img" + str(time.time()) + img_format, img2
            )
        else:
            img_diff = cv.hconcat([img1, img2])
            time_ = str(time.time())
            print(save_folder + "/Img")

            cv.imwrite(save_folder + "/Img" + time_ + img_format, img_diff)
            print(
                "Image has diff: {} ".format(score)
            )

img = Image()
img.compare_images("C:\Projects\Python\WatchUI\Img\img.png", "C:\Projects\Python\WatchUI\Img\img.png")