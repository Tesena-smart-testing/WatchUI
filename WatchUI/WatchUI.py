# -*- coding: utf-8 -*-
#
# This tool helps you compare images in robot framework
# It works with openCV + Python > 3.5
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY;
#
# Copyright (C) 2019-2020
#
# Authors: Jan "Procesor" Egermaier
#          Radek "bednaJedna" Bednařík


import cv2 as cv
from skimage.metrics import structural_similarity
import imutils
import os
import time
from robot.libraries.BuiltIn import BuiltIn
import csv
import pandas as pd


class WatchUI:
    seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
    robotlib = BuiltIn().get_library_instance("BuiltIn")
    save_folder_path = "../Outputs"
    starts_ssim = 1.0

    def __init__(self, outputs_folder="../Outputs", ssim_basic=starts_ssim):
        self.outputs_folder = outputs_folder
        self.ssim_basic = float(ssim_basic)

    def _check_dir(self, save_folder):
        outputs_folder = self.outputs_folder
        if save_folder != "../Outputs":
            if os.path.exists(save_folder):
                self.save_folder = save_folder
            else:
                os.mkdir(save_folder)
                self.save_folder = save_folder
        else:
            if os.path.exists(outputs_folder):
                self.save_folder = outputs_folder
            else:
                os.mkdir(outputs_folder)
                self.save_folder = outputs_folder

    def _check_ssim(self, ssim):
        if ssim == 1.0:
            self.ssim = self.ssim_basic
        else:
            self.ssim = ssim

    def _compare_images(self, path1, path2):
        img1 = cv.imread(path1, 1)
        img2 = cv.imread(path2, 1)

        # convert to grey
        gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        # SSIM diff Img
        (self.score, diff) = structural_similarity(gray_img1, gray_img2, full=True)
        diff = (diff * 255).astype("uint8")

        # Threshold diff Img
        thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
        cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        self.cnts = imutils.grab_contours(cnts)
        self.img1 = img1
        self.img2 = img2

    def compare_images(
        self, path1, path2, save_folder=save_folder_path, ssim=starts_ssim
    ):
        """Comparing images

        It compares two images from the two paths and, if there are differences, saves the image with the errors highlighted
        in the folder: ../Save Image

        path1 = path to the first image to be compared
        path2 = path to the second image to be compared

        Example: Compare two image ../image1.png ../Image2.png
        """
        self._check_dir(save_folder)
        self._check_ssim(ssim)
        save_folder = self.save_folder
        if os.path.exists(path1) and os.path.exists(path2):
            # Compare image
            self._compare_images(path1, path2)
            score = self.score

            # Create frame in diff area
            for c in self.cnts:
                (x, y, w, h) = cv.boundingRect(c)
                cv.rectangle(self.img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv.rectangle(self.img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Show image

            if float(score) < self.ssim:
                self.robotlib.log_to_console(self.ssim)
                self.robotlib.log_to_console(score)
                cv.imwrite(save_folder + "/Img" + str(time.time()) + ".png", self.img2)
                self.robotlib.fail("*INFO* Save file with difference")
        else:
            raise AssertionError("Path doesnt exists")

    def compare_screen(self, path1, save_folder=save_folder_path, ssim=starts_ssim):
        """	Compare the already save image with the browser screen

        Compares the already saved image with the screen that is on the screen. If there is a difference, it saves the
        highlighted image to the: ../Save Image

        path1 = path to the image to be compared to screen

        Example: Compare screen ../image1.png
        """
        self._check_dir(save_folder)
        self._check_ssim(float(ssim))
        save_folder = self.save_folder
        self.seleniumlib.capture_page_screenshot(save_folder + "/testscreen.png")
        path2 = save_folder + "/testscreen.png"
        if os.path.exists(path1):
            if os.path.exists(path2):
                # Compare image
                self._compare_images(path1, path2)
                score = self.score

                # Create frame in diff area
                for c in self.cnts:
                    (x, y, w, h) = cv.boundingRect(c)
                    cv.rectangle(self.img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv.rectangle(self.img2, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # Show image

                self.robotlib.log_to_console(self.ssim)
                if float(score) < self.ssim:
                    self.robotlib.log_to_console(self.ssim)
                    img_diff = cv.hconcat([self.img1, self.img2])
                    cas = str(time.time())
                    score_percen = float(score) * 100
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + "/Img" + cas + ".png"
                    )
                    cv.imwrite(save_folder + "/Img" + cas + ".png", img_diff)
                    self.robotlib.fail("Image has diff: {} %".format(score_percen))
                else:
                    img_diff = cv.hconcat([self.img1, self.img2])
                    cas = str(time.time())
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + "/Img" + cas + ".png"
                    )
                    cv.imwrite(save_folder + "/Img" + cas + ".png", img_diff)
                    self.robotlib.log_to_console("Image has diff: {} ".format(score))
            else:
                raise AssertionError("Path2 doesnt found:" + path2)
        else:
            raise AssertionError("Path1 doesnt found" + path1)
        if os.path.exists(save_folder + "/testscreen.png"):
            os.remove(save_folder + "/testscreen.png")

    def create_area(
        self, x1, y1, x2, y2, save_folder=save_folder_path, screen_name="screen"
    ):
        """  Creates a cut-out from the screen

        Creates a cut-out from the screen that is on screen and saves it in the folder: ../Create area

        x1 a y1 = x and y coordinates for the upper left corner of the square
        x2 and y2 = x and y coordinates for the bottom right corner of the square

        Example: Compare making area 0 0 25 25
        """
        self._check_dir(save_folder)
        save_folder = self.save_folder

        self.seleniumlib.capture_page_screenshot(save_folder + '/testscreen.png')
        img = save_folder + '/testscreen.png'
        img_crop = cv.imread(img)
        crop_img = img_crop[
            int(x1) : int(y2), int(y1) : int(x2)
        ]  # Crop from {x, y, w, h } => {0, 0, 300, 400}
        if screen_name == "screen":
            cv.imwrite(save_folder + '/screen' + str(time.time()) + '.png', crop_img)
        else:
            cv.imwrite(save_folder + '/' + screen_name + '.png', crop_img)

    def create_screens(
        self, *resolution, save_folder=save_folder_path, screen_name="screen"
    ):
        """ Creates a screenshot on the screen

        Creates a screenshot on the screen, that corresponds to the specified resolution, so it is possible to create on one
        page an infinite number of screens with different resolutions.
        Screens are stored in the folder: ../Create rescreens

        *resolutin = The specified resolution in width and height format, you can enter as many as needed

        Example: compare making rescreens 800 600 1280 800 1440 900 Creates 3 screens in 800x600 1280x800 and 1440x90
        """
        self._check_dir(save_folder)
        save_folder = self.save_folder

        leng_reso = len(resolution)
        if leng_reso % 2 == 0:

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
                    + ".png"
                )
                a += 2
                i += 1
        else:
            raise AssertionError("Bad numbers of resolution")

    def compare_screen_areas(
        self, x1, y1, x2, y2, path1, save_folder=save_folder_path, ssim=starts_ssim
    ):
        """Creates a cut-out from the screen

        Creates a cut-out from the screen that is on the screen and compares it to a previously created

        x1 and y1 = x and y coordinates for the upper left corner of the square
        x2 and y2 = x and y coordinates for the bottom right corner of the square
        path1 = Path to an already created viewport with which we want to compare the viewport created by us

        Example: Compare screen area 0 0 25 25 ../Crop_Image1.png Creates Crop_Image1.png from 0, 0, 25, 25
        """
        self._check_dir(save_folder)
        self._check_ssim(ssim)
        save_folder = self.save_folder
        self.seleniumlib.capture_page_screenshot(save_folder + '/test1.png')
        path2 = save_folder + '/test1.png'

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
                (score, diff) = structural_similarity(gray_img1, crop_img, full=True)
                diff = (diff * 255).astype('uint8')

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
                if float(score) < self.ssim:
                    self.robotlib = BuiltIn().get_library_instance('BuiltIn')
                    img_diff = cv.hconcat([img1, crop_img_color])
                    cas = str(time.time())
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + '/img' + cas + '.png'
                    )
                    cv.imwrite(save_folder + '/img' + cas + '.png', img_diff)
                    self.robotlib.fail('Image has diff: {} '.format(score))
                    score_percen = float(score) * +100
                    self.robotlib.fail('Image has diff: {} %'.format(score_percen))
            else:
                raise AssertionError("New screen doesnt exist anymore")
        else:
            raise AssertionError("You put bad path")
        if os.path.exists(save_folder + '/test1.png'):
            os.remove(save_folder + '/test1.png')

    def compare_screen_without_areas(
        self, path1, *args, save_folder=save_folder_path, ssim=starts_ssim
    ):
        """
        Compares two pictures, which have parts to be ignored
        x1 and y1 = x and y coordinates for the upper left corner of the ignored area square
        x2 and y2 = x and y coordinates for the lower right corner of the square of the ignored part

        Attention! It is always necessary to enter in order x1 y1 x2 y2 x1 y1 x2 y2 etc ...

        Compare screen without areas ../Image1.png 0 0 30 40 50 50 100 100
        Creates 2 ignored parts at 0,0, 30,40 and 50, 50, 100, 100
        """
        self._check_dir(save_folder)
        self._check_ssim(ssim)
        save_folder = self.save_folder

        self.seleniumlib.capture_page_screenshot(save_folder + "/test1.png")
        path2 = save_folder + "/test1.png"
        if os.path.exists(path1) and os.path.exists(path2):
            lt = len(args)
            img1 = cv.imread(path1, 1)
            img2 = cv.imread(path2, 1)
            if lt % 4 == 0:
                x = lt / 4
                self.robotlib.log_to_console(x)
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
                (score, diff) = structural_similarity(gray_img1, gray_img2, full=True)
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
                if float(score) < self.ssim:
                    img_diff = cv.hconcat([img1, img2])
                    cas = str(time.time())
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + "/Img" + cas + ".png"
                    )
                    cv.imwrite(save_folder + "/Img" + cas + ".png", img_diff)
                    self.robotlib.fail("Image has diff: {} ".format(score))
                else:
                    img_diff = cv.hconcat([img1, img2])
                    cas = str(time.time())
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + "/Img" + cas + ".png"
                    )
                    cv.imwrite(save_folder + "/Img" + cas + ".png", img_diff)
                    self.robotlib.log_to_console("Image has diff: {} ".format(score))
        else:
            raise AssertionError("Path doesnt exists")

    def compare_screen_get_information(
        self,
        path1,
        save_folder=save_folder_path,
        folder_csv="../CSV_ERROR",
        ssim=starts_ssim,
    ):
        """	Compare the already save image with the browser screen

        Compares the already saved image with the screen that is on the screen. If there is a difference, it saves the
        highlighted image to the: ../Save Image and making csv file with coordinates and elements which exist on this
        coordinates

        path1 = path to the image to be compared to screen

        Example: Compare screen ../image1.png
        """
        self._check_dir(save_folder)
        self._check_dir(folder_csv)
        self._check_ssim(ssim)
        save_folder = self.save_folder
        # Making screen
        self.seleniumlib.capture_page_screenshot(save_folder + "/test1.png")
        path2 = save_folder + "/test1.png"
        if os.path.exists(path1):
            if os.path.exists(path2):
                # load Img
                self._compare_images(path1, path2)
                score = self.score

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
                if float(score) < self.ssim:
                    img_diff = cv.hconcat([self.img1, self.img2])
                    cas = str(time.time())
                    self.seleniumlib.capture_page_screenshot(
                        save_folder + "/Img{0}.png".format(cas)
                    )
                    cv.imwrite(save_folder + "/Img{0}.png".format(cas), img_diff)

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

                    score_percen = float(score) * 100
                    self.robotlib.fail("Image has diff: {} %".format(score_percen))
            else:
                raise AssertionError("Bad or not exists path for picture or screen")
        else:
            raise AssertionError("Bad or not exists path for picture or screen")

