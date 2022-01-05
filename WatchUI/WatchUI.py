import csv
import os
import time
import cv2 as cv
import pandas as pd
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from skimage.metrics import structural_similarity
import pytesseract
import fitz
import imutils


__version__ = "1.0.12"


class WatchUI:
    """
    WatchUI is Robot Framework visual testing library for visual difference testing as well as image content testing (including PDF documents).
    Runs on Selenium or Playwright to generate screenshots, PyMuPDF to process PDFs and Tesseract OCR to recognize text.
    It allows visually test web sites, applications, PDFs or just compare bitmaps.


    %TOC%

    = Installation =

    Installation with pip: ``pip install watchui``

    For more details about set up check out our Quick start section on our website:
    https://tesena-smart-testing.github.io/WatchUI/start.html

    *IMPORTANT*: When you are using this library, screenshots must same resolution!

    = Example =
    | *** Settings ***
    | Library         WatchUI
    | Library         SeleniumLibrary
    |
    | *** Variables ***
    | ${URL}        https://www.tesla.com/
    | ${BROWSER}    chrome
    |
    | *** Test Cases ***
    | Sample test
    |    Compare screen with image
    |
    | *** Keywords ***
    | Compare screen with image
    |    Open Browser                        ${start_url}      ${browser}
    |    Set window size                     800     600
    |    Compare screen                      ./Outputs/screen800x600.png


    """

    ROBOT_LIBRARY_VERSION = __version__
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    save_folder_path = "./Outputs"
    starts_ssim = 1.0
    starts_format_image = "png"
    default_tesseract_path = ""

    def __init__(
        self,
        outputs_folder: str = save_folder_path,
        ssim_basic: float = starts_ssim,
        format_image: str = starts_format_image,
        tesseract_path: str = default_tesseract_path,
    ):
        """Library can be imported either with default output folder and set lowest limit of difference between images (``ssim``), or
        you can provide your own values.

        Keyword Arguments:

            ``outputs_folder`` path, where to save images with highlighted differences.

            ``ssim_basic`` threshold value in the interval (0, 1>. Tests are passed, if ssim value returned by keyword test functions is bigger than this.

            ``format_image`` format for saving picture / screenshot (png, jpg etc.) Example: ``format_image=jpg``.

        Examples:

        | =Setting= | =Value= | =Value= | =Value= | =Comment= |
        | Library   | WatchUI |      |  | # Uses default values of keyword arguments |
        | Library   | WatchUI | outputs_folder=<path_to_folder> | | # Sets output path to path_to_folder |
        | Library   | WatchUI | outputs_folder=<path_to_folder> | ssim_basic=<ssmi_threshold> | # Sets output path to path_to_folder and treshold to ssmi_threshold |

        """
        self.outputs_folder = outputs_folder
        self.ssim_basic = float(ssim_basic)
        self.image_format = str(format_image)
        self.tesseract_path = str(tesseract_path)
        self._set_tesseract_path(self.tesseract_path)

        # when libdoc builds documentation, this would lead to exception, since robot cannot access execution context,
        # since nothing really executes
        try:
            self.seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
            self.robotlib = BuiltIn().get_library_instance("BuiltIn")
        except RobotNotRunningError as e:
            print(
                f"If you are trying to build documentation, than this exception is just nuisance, skipping...\n{str(e)}"
            )
            pass
        self.score = None
        self.cnts = None
        self.img1 = None
        self.img2 = None

    def _check_dir(self, save_folder: str):
        """Checks, if given ``save_folder`` exists, if not, creates it.

        Arguments:
            ``save_folder`` Path to <save_folder>
        """
        if save_folder != self.save_folder_path:
            if os.path.exists(save_folder):
                self.save_folder = save_folder
            else:
                os.mkdir(save_folder)
                self.save_folder = save_folder
        else:
            if os.path.exists(self.outputs_folder):
                self.save_folder = self.outputs_folder
            else:
                os.mkdir(self.outputs_folder)
                self.save_folder = self.outputs_folder

    def _check_ssim(self, ssim: float):
        """Checks, if ssim equals default, returns ``ssim`` value.

        Arguments:
            ``ssim`` Provided ssim value

        Returns:
            self.ssim {float} -- ssim value as instance attribute
        """
        if ssim == 1.0:
            self.ssim = float(self.ssim_basic)
        else:
            self.ssim = float(ssim)

    def _check_image_format(self, format: str):
        """Checks, which format setup for saving picture.

        Arguments:
            ``format_image`` Image format as png, jpg etc.

        Returns:
            ``self.format`` {float} Format for setup image type.
        """
        if str(format) == "png":
            self.format = "." + self.image_format
        else:
            self.format = "." + format

    def _compare_images(self, path1: str, path2: str):
        """Compares two images.

        Arguments:
            ``path1`` Filepath to image 1
            ``path2`` Filepath to image 2
        """
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

    def _set_tesseract_path(self, path_to_tesseract: str):
        """
        Checks, if given ``path_to_tess`` is same as default, is not return new path.

        Arguments:
            ``path`` path to <save_folder>
        """
        if path_to_tesseract:
            pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

    # ======================================== Keywords ========================================================

    def compare_images(
        self,
        path1: str,
        path2: str,
        save_folder: str = save_folder_path,
        ssim: float = starts_ssim,
        image_format: str = starts_format_image,
    ):
        """Compare two images. If there are differences, saves the image with the errors highlighted in the folder: save_folder_path

        ``path1`` = path to the first image to be compared
        ``path2`` = path to the second image to be compared

        Example:
        | Compare Images | ../image1.png | ../image2.png

        """
        self._check_dir(save_folder)
        self._check_ssim(ssim)
        self._check_image_format(image_format)

        if os.path.exists(path1) and os.path.exists(path2):
            # Compare image
            self._compare_images(path1, path2)

            # Create frame in diff area
            for c in self.cnts:
                (x, y, w, h) = cv.boundingRect(c)
                cv.rectangle(self.img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv.rectangle(self.img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Show image

            if float(self.score) < self.ssim:
                self.robotlib.log(self.ssim)
                self.robotlib.log(self.score)
                time_ = str(time.time())
                cv.imwrite(self.save_folder + "/Img" + time_ + self.format, self.img2)
                img_url = self.save_folder + "/Img" + time_ + self.format
                self.robotlib.log(message="<img src=" + str(img_url) + ">", html=True)
                self.robotlib.fail("*INFO* Save file with difference1")
            else:
                img_diff = cv.hconcat([self.img1, self.img2])
                time_ = str(time.time())
                self.seleniumlib.capture_page_screenshot(
                    save_folder + "/Img" + time_ + self.format
                )
                cv.imwrite(save_folder + "/Img" + time_ + self.format, img_diff)
                self.robotlib.log("Image has diff: {} ".format(self.score))
                img_url = save_folder + "/Img" + time_ + self.format
                self.robotlib.log(message="<img src=" + str(img_url) + ">", html=True)

        else:
            raise AssertionError(
                "The path ["
                + path1
                + "] or ["
                + path2
                + "] to the image does not exist."
            )

    def compare_screen(
        self,
        path1: str,
        save_folder: str = save_folder_path,
        ssim: float = starts_ssim,
        image_format: str = starts_format_image,
    ):
        """Compare the already saved image with the browser screen.

        Compares the already saved image with the screen / browser that is open. If there is a difference, it saves the
        highlighted image to the: save_folder_path

        ``path1`` = Path to the image to be compared to screen

        Example:
        | Compare Screen | ../image1.png
        """
        self._check_dir(save_folder)
        self._check_ssim(float(ssim))
        self._check_image_format(image_format)
        save_folder = self.save_folder
        self.seleniumlib.capture_page_screenshot(save_folder + "/testscreen.png")
        path2 = save_folder + "/testscreen.png"
        if os.path.exists(path1):
            if os.path.exists(path2):
                # Compare image
                self._compare_images(path1, path2)

                # Create frame in diff area
                for c in self.cnts:
                    (x, y, w, h) = cv.boundingRect(c)
                    cv.rectangle(self.img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv.rectangle(self.img2, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # Show image

                self.robotlib.log(self.ssim)
                if float(self.score) < self.ssim:
                    self.robotlib.log(self.ssim)
                    img_diff = cv.hconcat([self.img1, self.img2])
                    time_ = str(time.time())
                    score_percen = float(self.score) * 100
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + "/Img" + time_ + self.format
                    )
                    cv.imwrite(save_folder + "/Img" + time_ + self.format, img_diff)
                    self.robotlib.fail("Image has diff: {} %".format(score_percen))
                else:
                    img_diff = cv.hconcat([self.img1, self.img2])
                    time_ = str(time.time())
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + "/Img" + time_ + self.format
                    )
                    cv.imwrite(save_folder + "/Img" + time_ + self.format, img_diff)
                    self.robotlib.log("Image has diff: {} ".format(self.score))
            else:
                raise AssertionError(
                    "The path2 to the image does not exist. Try a other path, than:"
                    + path2
                )
        else:
            raise AssertionError(
                "The path1 to the image does not exist. Try a other path, than:" + path1
            )
        if os.path.exists(save_folder + "/testscreen.png"):
            os.remove(save_folder + "/testscreen.png")

    def create_area(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        save_folder: str = save_folder_path,
        screen_name: str = "screen",
        image_format: str = starts_format_image,
    ):
        """Creates a cut-out from the screen

        Creates a cut-out from the screen that is on screen and saves it in the folder: ``save_folder``

        ``x1`` and ``y1`` = x and y coordinates for the upper left corner of the square
        ``x2`` and ``y2`` = x and y coordinates for the bottom right corner of the square

        Example:
        | Create Area | 0 | 0 | 25 | 25 |
        """
        self._check_dir(save_folder)
        save_folder = self.save_folder
        self._check_image_format(image_format)

        self.seleniumlib.capture_page_screenshot(save_folder + "/testscreen.png")
        img = save_folder + "/testscreen.png"
        img_crop = cv.imread(img)
        crop_img = img_crop[int(y1) : int(y1) + int(y2), int(x1) : int(x1) + int(x2)]
        if screen_name == "screen":
            cv.imwrite(
                save_folder + "/screen" + str(time.time()) + self.format, crop_img
            )
        else:
            cv.imwrite(save_folder + "/" + screen_name + self.format, crop_img)

    def create_screens(
        self,
        *resolution: int,
        save_folder: str = save_folder_path,
        screen_name: str = "screen",
        image_format: str = starts_format_image,
    ):
        """Creates a screenshots on the screen

        Creates a screenshots on the screen, that corresponds to the specified resolution. It is also possible to create on
        one page an infinite number of screens with different resolutions.
        Screens are stored in the folder: ``save_folder``

        ``*resolution`` = The specified resolution in width and height format, you can enter as many as needed

        Warning: When you create one screen, name will be screen.png, but when you create more than one screen from same
        page, name will be screen screen_name_width_height.png

        Example to create 3 screens in 800x600 1280x800 and 1440x90
        | Create Screens | 800 | 600 | 1280 | 800 | 1440 | 900 |
        """
        self._check_dir(save_folder)
        save_folder = self.save_folder
        self._check_image_format(image_format)

        leng_reso = len(resolution)
        if leng_reso % 2 == 0:
            if (leng_reso / 2) == 1:
                self.seleniumlib.set_window_size(int(resolution[0]), int(resolution[1]))
                time.sleep(1)
                self.seleniumlib.capture_page_screenshot(
                    save_folder + "/" + screen_name + self.format
                )
            else:
                x = leng_reso / 2
                i = 0
                a = 0
                while i < x:
                    width = int(resolution[0 + a])
                    height = int(resolution[1 + a])
                    self.seleniumlib.set_window_size(width, height)
                    time.sleep(1)
                    self.seleniumlib.capture_page_screenshot(
                        save_folder
                        + "/"
                        + screen_name
                        + str(width)
                        + "x"
                        + str(height)
                        + self.format
                    )
                    a += 2
                    i += 1
        else:
            raise AssertionError(
                "Incorrect number of resolutions. It is expected even number of resolution parameters [width x height] but is seems to be odd:"
                + leng_reso
            )

    def compare_screen_areas(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        path1: str,
        save_folder: str = save_folder_path,
        ssim: float = starts_ssim,
        image_format=starts_format_image,
    ):
        """Creates a cut-out from the screen that is on the screen and compares it to a previously created

        ``x1`` and ``y1`` = x and y coordinates for the upper left corner of the square
        ``x2`` and ``y2`` = x and y coordinates for the bottom right corner of the square
        ``path1`` = Path to an already created viewport with which we want to compare the viewport created by us

        Example:
        | Compare Screen Areas | 0 | 0 | 25 | 25 | ../cropped_image1.png |
        """
        self._check_dir(save_folder)
        self._check_ssim(ssim)
        self._check_image_format(image_format)
        save_folder = self.save_folder
        self.seleniumlib.capture_page_screenshot(save_folder + "/test1.png")
        path2 = save_folder + "/test1.png"

        if os.path.exists(path1):
            if os.path.exists(path2):
                # load img
                img1 = cv.imread(path1, 1)  # img from docu
                img2 = cv.imread(path2, 1)  # img from screenshot

                # convert to grey
                gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
                gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

                # spliting area
                crop_img = gray_img2[
                    int(x1) : int(y2), int(y1) : int(x2)
                ]  # Crop from {x, y, w, h } => {0, 0, 300, 400}

                # SSIM diff img
                (self.score, diff) = structural_similarity(
                    gray_img1, crop_img, full=True
                )
                diff = (diff * 255).astype("uint8")

                # Threshold diff img
                thresh = cv.threshold(
                    diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU
                )[1]
                cnts = cv.findContours(
                    thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
                )
                cnts = imutils.grab_contours(cnts)

                crop_img_color = img2[int(x1) : int(y2), int(y1) : int(x2)]
                # Create frame in diff area
                for c in cnts:
                    (x, y, w, h) = cv.boundingRect(c)
                    cv.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv.rectangle(crop_img_color, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # Show image
                if float(self.score) < self.ssim:
                    self.robotlib = BuiltIn().get_library_instance("BuiltIn")
                    img_diff = cv.hconcat([img1, crop_img_color])
                    time_ = str(time.time())
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + "/img" + time_ + ".png"
                    )
                    cv.imwrite(save_folder + "/img" + time_ + self.format, img_diff)
                    self.robotlib.fail("Image has diff: {} ".format(self.score))
                    score_percen = float(self.score) * +100
                    self.robotlib.fail("Image has diff: {} %".format(score_percen))
                else:
                    img_diff = cv.hconcat([self.img1, self.img2])
                    time_ = str(time.time())
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + "/Img" + time_ + self.format
                    )
                    cv.imwrite(save_folder + "/Img" + time_ + self.format, img_diff)
                    self.robotlib.log("Image has diff: {} ".format(self.score))
            else:
                raise AssertionError("New screen does not exist anymore.")
        else:
            raise AssertionError(
                "The path1 to the image does not exist. Try a other path, than:" + path1
            )
        if os.path.exists(save_folder + "/test1.png"):
            os.remove(save_folder + "/test1.png")

    def compare_screen_without_areas(
        self,
        path1,
        *args,
        save_folder=save_folder_path,
        ssim=starts_ssim,
        image_format=starts_format_image,
    ):
        """
        Compares picture with actual open browser window, with areas to be ignored.
        ``x1`` and ``y1`` = x and y coordinates for the upper left corner of the ignored area square
        ``x2`` and ``y2`` = x and y coordinates for the lower right corner of the square of the ignored part

        Attention! It is always necessary to enter in right order ``x1`` ``y1`` ``x2`` ``y2`` ``x1`` ``y1`` ``x2`` ``y2`` etc.

        Example: Compare picture from ``path1`` with open browser and ignore its 2 parts at [``0``, ``0``, ``30``, ``40``] and [``50``, ``50``, ``100``, ``100``]
        | Compare Screen Without Areas | ../Image1.png | 0 | 0 | 30 | 40 | 50 | 50 | 100 | 100 |
        """
        self._check_dir(save_folder)
        self._check_ssim(ssim)
        self._check_image_format(image_format)
        save_folder = self.save_folder

        self.seleniumlib.capture_page_screenshot(save_folder + "/test1.png")
        path2 = save_folder + "/test1.png"
        if os.path.exists(path1) and os.path.exists(path2):
            lt = len(args)
            img1 = cv.imread(path1, 1)
            img2 = cv.imread(path2, 1)
            if lt % 4 == 0:
                x = lt / 4
                self.robotlib.log(x)
                i = 0
                a = 0
                while i < x:
                    color = (0, 0, 0)
                    x1 = int(args[0 + a])
                    y1 = int(args[1 + a])
                    x2 = int(args[2 + a])
                    y2 = int(args[3 + a])

                    cv.rectangle(img1, (x1, y1), (x2, y2), color, -1)
                    cv.rectangle(img2, (x1, y1), (x2, y2), color, -1)
                    a += 4
                    i += 1
                cv.namedWindow("image", cv.WINDOW_NORMAL)

                # convert to grey
                gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
                gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

                # SSIM diff Img
                (self.score, diff) = structural_similarity(
                    gray_img1, gray_img2, full=True
                )
                diff = (diff * 255).astype("uint8")

                # Threshold diff Img
                thresh = cv.threshold(
                    diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU
                )[1]
                cnts = cv.findContours(
                    thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
                )
                cnts = imutils.grab_contours(cnts)

                # Create frame in diff area
                for c in cnts:
                    (x, y, w, h) = cv.boundingRect(c)
                    cv.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # Show image
                if float(self.score) < self.ssim:
                    img_diff = cv.hconcat([img1, img2])
                    time_ = str(time.time())
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + "/Img" + time_ + self.format
                    )
                    cv.imwrite(save_folder + "/Img" + time_ + self.format, img_diff)
                    self.robotlib.fail("Image has diff: {} ".format(self.score))
                else:
                    img_diff = cv.hconcat([img1, img2])
                    time_ = str(time.time())
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + "/Img" + time_ + self.format
                    )
                    cv.imwrite(save_folder + "/Img" + time_ + self.format, img_diff)
                    self.robotlib.log("Image has diff: {} ".format(self.score))
        else:
            raise AssertionError(
                "The path ["
                + path1
                + "] or ["
                + path2
                + "] to the image does not exist."
            )

    def compare_screen_get_information(
        self,
        path1,
        save_folder=save_folder_path,
        folder_csv="../CSV_ERROR",
        ssim=starts_ssim,
        image_format=starts_format_image,
    ):
        """Compares the already saved image with the screen that is on the screen. If there is a difference, it saves the
        highlighted image to the: ``save_folder`` and creates csv file with coordinates and elements which exist on this
        coordinates.

        ``path1`` = path to the image to be compared to screen

        Example:
        | Compare screen | ../image1.png |
        """
        self._check_dir(save_folder)
        self._check_dir(folder_csv)
        self._check_ssim(ssim)
        self._check_image_format(image_format)
        save_folder = self.save_folder
        # Making screen
        self.seleniumlib.capture_page_screenshot(save_folder + "/test1.png")
        path2 = save_folder + "/test1.png"
        if os.path.exists(path1):
            if os.path.exists(path2):
                # load Img
                self._compare_images(path1, path2)

                # write coordinate
                with open(folder_csv + "/bug_coordinates.csv", "w") as csvfile:
                    writer = csv.writer(csvfile)
                    a = "path", "x_center", "y_center", "x", "y", "x1", "y1"
                    writer.writerow(a)

                    # Create frame in diff area
                    for c in self.cnts:
                        (x, y, w, h) = cv.boundingRect(c)
                        cv.rectangle(self.img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        cv.rectangle(self.img2, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        x2 = x + w
                        y2 = y + h
                        x_center = x + ((x2 - x) / 2)
                        y_center = y + ((y2 - y) / 2)
                        f = path1, x_center, y_center, x, y, x2, y2
                        writer.writerow(f)

                # Save image and show report
                if float(self.score) < self.ssim:
                    img_diff = cv.hconcat([self.img1, self.img2])
                    time_ = str(time.time())
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + "/Img{0}.{1}".format(time_, self.format)
                    )
                    cv.imwrite(
                        save_folder + "/Img{0}.{1}".format(time_, self.format), img_diff
                    )

                    # start reading coordinates and saving element from coordinate
                    df = pd.read_csv(r"" + folder_csv + "/bug_coordinates.csv")
                    with open(
                        folder_csv + "/bug_co_and_name{0}.csv".format(str(time.time())),
                        "w",
                    ) as csv_name:
                        writer = csv.writer(csv_name)
                        a = "web-page", "x_center", "y_center", "class", "id", "name"
                        writer.writerow(a)

                        # Get information from position
                        for i in range(len(df)):
                            x_center = df.values[i, 1]
                            y_center = df.values[i, 2]
                            driver = self.seleniumlib.driver
                            elements = driver.execute_script(
                                "return document.elementsFromPoint(arguments[0], arguments[1]);",
                                x_center,
                                y_center,
                            )
                            for element in elements:
                                e_class = element.get_attribute("class")
                                e_id = element.get_attribute("id")
                                e_name = element.get_attribute("name")
                                f = path1, x_center, y_center, e_class, e_id, e_name
                                writer.writerow(f)

                    score_percen = float(self.score) * 100
                    self.robotlib.fail("Image has diff: {} %".format(score_percen))
            else:
                raise AssertionError("Bad or not exists path for picture or screen.")
        else:
            raise AssertionError("Bad or not existing path for picture or screen.")

    # ------------------------------------------ Tesseract / PDF ----------------------------------------------------------#

    def image_to_string(
        self, path: str, oem: int = "3", psm="3", language: str = "eng"
    ):
        """
        Read text from image. For proper functionality  tesseract-ocr must be installed.

        ``path`` = Path to the image, which we wanna read
        ``oem`` = Engine Mode (Settings from tesseract)
        ``psm`` = Page Segmentation Mode (Settings from tesseract)
        ``language`` = The Language we wanna read file
        ``path_to_tesseract`` = Path to root folder with tesseract.exe
        """
        if os.path.exists(path):
            old_img = cv.imread(path)
            custom_oem_psm_config = r"--oem " + oem + " --psm " + psm
            text = pytesseract.image_to_string(
                old_img, config=custom_oem_psm_config, lang=language
            )
            return text
        else:
            raise AssertionError("Path " + path + " does not exists")

    def image_area_on_text(
        self, path: str, *coordinates: int, oem="3", psm="3", language: str = "eng"
    ):
        """
        Read text from image.
        Note: This keyword requires tesseract-ocr to be installed.

        ``path`` = Path to the image to be transformed into text
        ``*coordinates`` = Coordinates where text is located. Must be 4 (x1, y1, x2, y2)
        ``oem`` = Engine Mode (Settings from tesseract)
        ``psm`` = Page Segmentation Mode (Settings from tesseract)
        ``language`` = Language of text on bitmap which to be transformed to text file

        """
        string_list = []
        old_img = cv.imread(path)
        len_coordinates = len(coordinates)
        if os.path.exists(path):

            if len_coordinates % 4 == 0:
                if len_coordinates / 4 == 1:
                    crop_img = old_img[
                        int(coordinates[1]) : int(coordinates[3]),
                        int(coordinates[0]) : int(coordinates[2]),
                    ]
                    custom_oem_psm_config = r"--oem " + oem + " --psm " + psm
                    text = pytesseract.image_to_string(
                        crop_img, config=custom_oem_psm_config, lang=language
                    )
                    # delete blank line space
                    text = os.linesep.join([s for s in text.splitlines() if s])
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
                        crop_img = old_img[int(y1) : int(y2), int(x1) : int(x2)]
                        custom_oem_psm_config = r"--oem " + oem + " --psm " + psm
                        text = pytesseract.image_to_string(
                            crop_img, config=custom_oem_psm_config, lang=language
                        )
                        string_list.append(text)
                        i += 1
                        a += 4
                    return string_list
            else:
                raise AssertionError(
                    "Number of coordinates for image areas to be processed is expected to be dividable by four but it seem to be not. "
                    + "Actual number of provided coordinates is "
                    + len_coordinates
                )
        else:
            raise AssertionError("Path " + path + " does not exists.")

    def pdf_to_image(
        self,
        path1: str,
        save_folder: str = save_folder_path,
        name: str = "img",
        number_page: int = "-1",
        zoom: int = "3",
    ):
        """Convert PDF to image.

        ``path`` = Path to the PDF file, which will be converted to image.
        ``name`` = Image name to created by converting PDF.
        ``number_page`` = PDF page number to be converted into image. If not set all pages will be processed.

        """

        self._check_dir(save_folder)
        save_folder = self.save_folder

        zoom = int(zoom)
        mat = fitz.Matrix(zoom, zoom)
        if os.path.exists(path1):
            doc = fitz.open(path1)
            if number_page == "-1":
                page_count = doc.pageCount
                for x in range(0, page_count):
                    page = doc.load_page(x)  # load all pages one by one
                    pix = page.get_pixmap(matrix=mat)
                    output = save_folder + "/" + name + "_" + str(x) + ".png"
                    pix.save(output)
            else:
                page = doc.load_page(int(number_page))  # number of page
                pix = page.get_pixmap(matrix=mat)
                output = save_folder + "/" + name + ".png"
                pix.save(output)
        else:
            raise AssertionError("Path " + path1 + " doesn't exists")

    def rotate_image(
        self,
        path: str,
        screen_name: str = "rotate_screen",
        save_folder=save_folder_path,
        rotate=0,
        image_format=starts_format_image,
    ):
        """Rotate image.

        ``path`` = Path to the image to be rotated.
        ``rotate`` = Angle to be rotated: 0 = 90 degrees clockwise, 1 = 90 degrees counter-clockwise, 2 = 180 degrees
        ``number_page`` = PDF page number to be converted into image.

        """
        self._check_dir(save_folder)
        save_folder = self.save_folder
        self._check_image_format(image_format)
        if os.path.exists(path):
            img = cv.imread(path)
            if int(rotate) == 0:
                rotate_image = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
                cv.imwrite(save_folder + "/" + screen_name + self.format, rotate_image)
            elif int(rotate) == 1:
                rotate_image = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
                cv.imwrite(save_folder + "/" + screen_name + self.format, rotate_image)
            elif int(rotate) == 2:
                rotate_image = cv.rotate(img, cv.ROTATE_180)
                cv.imwrite(save_folder + "/" + screen_name + self.format, rotate_image)
            else:
                raise AssertionError(
                    "You are trying to set rotation angle to: "
                    + str(rotate)
                    + " which is not allowed value. Allowed values are 0, 1 or 2. Please see documentations for more details."
                )
        else:
            raise AssertionError("Path" + path + "does not exists.")

    @staticmethod
    def return_text_from_area(
        path: str, page_number: int, x1: float, y1: float, x2: float, y2: float
    ):
        """
        Return text from area.
        It does not use tesseract, so it can be used on for standart PDF reading or without installed tesseract.

        ``path`` = Path to PDF to be processed
        ``page_number`` = PDF page number where text to be searched
        ``x1``, ``y1``, ``x2``, ``y2`` = coordinates where text to be searched
        """
        if os.path.exists(path):
            doc = fitz.open(path)
            page = doc[page_number]
            words_list = page.get_text_words()
            text = ""
            xy_numbers = 1
            for xy in words_list:
                if (
                    float(xy[0]) > float(x1)
                    and float(xy[1]) > float(y1)
                    and float(xy[2]) < float(x2)
                    and float(xy[3]) < float(y2)
                ):
                    if xy_numbers == len(words_list):
                        text += xy[4]
                    else:
                        text += xy[4] + " "
                xy_numbers += 1
            return text
        else:
            raise AssertionError("Cannot find file: " + path)

    @staticmethod
    def should_exist_this_text(path: str, page_number: int, text: str):
        """Returns ``true`` if ``text`` is found on page.

        ``path`` = Path to PDF to be processed
        ``page_number`` = PDF page number where text to be checked
        ``text`` = Text which we search for

        """
        if os.path.exists(path):
            doc = fitz.open(path)
            page = doc[page_number]
            text_instances = page.search_for(text)
            if len(text_instances) > 0:
                return True
            else:
                return False
        else:
            raise AssertionError("Cannot find file: " + path)

    def create_area_from_image(
        self,
        x1,
        y1,
        x2,
        y2,
        path1,
        save_folder=save_folder_path,
        screen_name="screen",
        image_format=starts_format_image,
    ):
        """Creates a cut-out from the image.
        Creates a cut-out from the screen that is on screen and saves it in the folder: ../Outputs

        ``x1`` and ``y1`` = x and y coordinates for the upper left corner of the square
        ``x2`` and ``y2`` = x and y coordinates for the bottom right corner of the square

        Example:
        | Compare Area From Image | 0 | 0 | 25 | 25 |
        """
        self._check_dir(save_folder)
        save_folder = self.save_folder
        self._check_image_format(image_format)

        if os.path.exists(path1):
            img = path1
            img_crop = cv.imread(img)
            crop_img = img_crop[
                int(y1) : int(y1) + int(y2), int(x1) : int(x1) + int(x2)
            ]
            if screen_name == "screen":
                cv.imwrite(
                    save_folder + "/screen" + str(time.time()) + self.format, crop_img
                )
            else:
                cv.imwrite(save_folder + "/" + screen_name + self.format, crop_img)
        else:
            raise AssertionError("Cannot find file: " + path1)
