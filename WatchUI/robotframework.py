# -*- coding: utf-8 -*-
#
# This tool helps you compare images in robot framework
# It works with openCV + Python > 3.5
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY;
#
# Copyright (C) 2019-2020
#
# Authors:  Jan "Procesor" Egermaier
#           Radek Bednařík

import cv2 as cv
from skimage.metrics import structural_similarity
import imutils
import os
import time
from robot.libraries.BuiltIn import BuiltIn
import csv
import pandas as pd


def _check_dir(save_folder: str) -> None:
    """Checks, if given folder exists, if not, then creates it.
    
    Arguments:
        save_folder {str} -- relative path to folder
    """
    if os.path.exists(save_folder):
        print(f"*INFO* Folder {save_folder} exists")
    else:
        os.mkdir(save_folder)
        print(f"*INFO* Folder {save_folder} crated")


def compare_two_image(path1, path2, save_folder="../Compare two Images"):
    """Comparing two images

    It compares two images from the two paths and, if there are differences, saves the image with the errors highlighted
    in the folder: ../Save Image

    path1 = path to the first image to be compared
    path2 = path to the second image to be compared

    Example: Compare two image ../image1.png ../Image2.png
    """
    _check_dir(save_folder)
    # if os.path.exists(save_folder):
    #     print("*INFO* Folder /Save Image exists")
    # else:
    #     os.mkdir(save_folder)
    #     print("*INFO* Folder /Save Image crated")
    if os.path.exists(path1) and os.path.exists(path2):
        # load img
        img1 = cv.imread(path1, 1)
        img2 = cv.imread(path2, 1)

        # convert to grey
        gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        # SSIM diff img
        (score, diff) = structural_similarity(gray_img1, gray_img2, full=True)
        diff = (diff * 255).astype("uint8")
        print("*INFO* SSIM: {}".format(score))

        # Threshold diff img
        thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
        cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # Create frame in diff area
        for c in cnts:
            (x, y, w, h) = cv.boundingRect(c)
            cv.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Show image
        print(score)
        if int(score) < 1.0:
            robotlib = BuiltIn().get_library_instance("BuiltIn")
            cv.imwrite(save_folder + "/img" + str(time.time()) + ".png", img2)
            robotlib.fail("*INFO* Save file with difference")
    else:
        raise AssertionError("Path doesnt exists")


def compare_screen(path1, save_folder="../Save Image"):
    """	Compare the already save image with the browser screen

    Compares the already saved image with the screen that is on the screen. If there is a difference, it saves the
    highlighted image to the: ../Save Image

    path1 = path to the image to be compared to screen

    Example: Compare screen ../image1.png
    """
    _check_dir(save_folder)
    seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
    seleniumlib.capture_page_screenshot(save_folder + "/testscreen.png")
    path2 = save_folder + "/testscreen.png"
    if os.path.exists(path1):
        if os.path.exists(path2):
            # load img
            img1 = cv.imread(path1, 1)
            img2 = cv.imread(path2, 1)

            # convert to grey
            gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
            gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

            # SSIM diff img
            (score, diff) = structural_similarity(gray_img1, gray_img2, full=True)
            diff = (diff * 255).astype("uint8")

            # Threshold diff img
            thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[
                1
            ]
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
            if int(score) < 1.0:
                robotlib = BuiltIn().get_library_instance("BuiltIn")
                # TODO: Add screen to log
                img_diff = cv.hconcat([img1, img2])
                cas = str(time.time())
                score_percen = float(score) * +100
                seleniumlib.capture_page_screenshot(save_folder + "/img" + cas + ".png")
                cv.imwrite(save_folder + "/img" + cas + ".png", img_diff)
                print("score" + str(score))
                robotlib.fail("Image has diff: {} %".format(score_percen))

        else:
            raise AssertionError("Path2 doesnt found")
    else:
        raise AssertionError("Path1 doesnt found")
    if os.path.exists(save_folder + "/testscreen.png"):
        os.remove(save_folder + "/testcreen.png")


def compare_making_area(x1, y1, x2, y2, save_folder="../Create area"):
    """  Creates a cut-out from the screen

    Creates a cut-out from the screen that is on screen and saves it in the folder: ../Create area

    x1 a y1 = x and y coordinates for the upper left corner of the square
    x2 and y2 = x and y coordinates for the bottom right corner of the square

    Example: Compare making area 0 0 25 25
    """
    _check_dir(save_folder)
    # if os.path.exists(save_folder):
    #     print("Folder exists")
    # else:
    #     os.mkdir(save_folder)
    seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
    seleniumlib.capture_page_screenshot(save_folder + "/testscreen.png")
    img = save_folder + "/testscreen.png"
    img_crop = cv.imread(img)
    crop_img = img_crop[
        int(x1) : int(y2), int(y1) : int(x2)
    ]  # Crop from {x, y, w, h } => {0, 0, 300, 400}
    cv.imwrite(save_folder + "/img" + str(time.time()) + ".png", crop_img)


def compare_making_rescreens(
    *resolution, save_folder="../Create rescreens", name_screen="rescreen"
):
    """ Creates a screenshot on the screen

    Creates a screenshot on the screen, that corresponds to the specified resolution, so it is possible to create on one
    page an infinite number of screens with different resolutions.
    Screens are stored in the folder: ../Create rescreens

    *resolutin = The specified resolution in width and height format, you can enter as many as needed

    Example: compare making rescreens 800 600 1280 800 1440 900 Creates 3 screens in 800x600 1280x800 and 1440x90
    """
    _check_dir(save_folder)
    seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
    robotlib = BuiltIn().get_library_instance("BuiltIn")
    time.sleep(2)
    leng_reso = len(resolution)
    if leng_reso % 2 == 0:
        robotlib.log_to_console(resolution)

        x = leng_reso / 2
        i = 0
        a = 0
        while i < x:
            width = int(resolution[0 + a])
            height = int(resolution[1 + a])

            seleniumlib.set_window_size(width, height)
            time.sleep(1)
            seleniumlib.capture_page_screenshot(
                save_folder
                + "/"
                + name_screen
                + str(width)
                + "x"
                + str(height)
                + ".png"
            )
            a += 2
            i += 1
    else:
        raise AssertionError("Bad numbers of resolution")


def compare_screen_area(x1, y1, x2, y2, path1, save_folder="../Save Image area"):
    """Creates a cut-out from the screen

    Creates a cut-out from the screen that is on the screen and compares it to a previously created

    x1 and y1 = x and y coordinates for the upper left corner of the square
    x2 and y2 = x and y coordinates for the bottom right corner of the square
    path1 = Path to an already created viewport with which we want to compare the viewport created by us

    Example: Compare screen area 0 0 25 25 ../Crop_Image1.png Creates Crop_Image1.png from 0, 0, 25, 25
    """
    _check_dir(save_folder)
    seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
    seleniumlib.capture_page_screenshot(save_folder + "/test_screen.png")
    path2 = save_folder + "/test_screen.png"
    if os.path.exists(path1):
        if os.path.exists(path2):
            # load img
            img1 = cv.imread(path1, 1)
            img2 = cv.imread(path2, 1)

            # convert to grey
            gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
            gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

            # spliting area
            crop_img = gray_img2[
                int(x1) : int(y2), int(y1) : int(x2)
            ]  # Crop from {x, y, w, h } => {0, 0, 300, 400}

            # SSIM diff img
            (score, diff) = structural_similarity(gray_img1, crop_img, full=True)
            diff = (diff * 255).astype("uint8")
            print("SSIM: {}".format(score))

            # Threshold diff img
            thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[
                1
            ]
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
            print(score)
            if int(score) < 1.0:
                robotlib = BuiltIn().get_library_instance("BuiltIn")
                # TODO: Add screen to log
                img_diff = cv.hconcat([img1, img2])
                cas = str(time.time())
                seleniumlib.capture_page_screenshot(save_folder + "/img" + cas + ".png")
                cv.imwrite(save_folder + "/img" + cas + ".png", img_diff)
                print("score" + str(score))
                robotlib.fail("Image has diff: {} ".format(score))
                score_percen = float(score) * +100
                print("score" + str(score))
                robotlib.fail("Image has diff: {} %".format(score_percen))
        else:
            raise AssertionError("New screen doesnt exist anymore")
    else:
        raise AssertionError("You put bad path")
    if os.path.exists(save_folder + "/test_screen.png"):
        os.remove(save_folder + "/test_screen.png")


def compare_screen_without_areas(path1, *args, save_folder="../Save Image areas"):
    """
    Compares two pictures, which have parts to be ignored
    x1 and y1 = x and y coordinates for the upper left corner of the ignored area square
    x2 and y2 = x and y coordinates for the lower right corner of the square of the ignored part

    Attention! It is always necessary to enter in order x1 y1 x2 y2 x1 y1 x2 y2 etc ...

    Compare screen without areas ../Image1.png 0 0 30 40 50 50 100 100
    Creates 2 ignored parts at 0,0, 30,40 and 50, 50, 100, 100
    """
    _check_dir(save_folder)
    seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
    seleniumlib.capture_page_screenshot(save_folder + "/test_screen.png")
    path2 = save_folder + "/test_screen.png"
    if os.path.exists(path1) and os.path.exists(path2):
        lt = len(args)
        img1 = cv.imread(path1, 1)
        img2 = cv.imread(path2, 1)
        if lt % 4 == 0:
            robotlib = BuiltIn().get_library_instance("BuiltIn")
            x = lt / 4
            robotlib.log_to_console(x)
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

            # SSIM diff img
            (score, diff) = structural_similarity(gray_img1, gray_img2, full=True)
            diff = (diff * 255).astype("uint8")
            print("SSIM: {}".format(score))

            # Threshold diff img
            thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[
                1
            ]
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
            print(score)
            if int(score) < 1.0:
                robotlib = BuiltIn().get_library_instance("BuiltIn")
                # TODO: Add screen to log
                img_diff = cv.hconcat([img1, img2])
                cas = str(time.time())
                seleniumlib.capture_page_screenshot(save_folder + "/img" + cas + ".png")
                cv.imwrite(save_folder + "/img" + cas + ".png", img_diff)
                robotlib.fail("Image has diff: {} ".format(score))
    else:
        raise AssertionError("Path doesnt exists")


# TODO Create keyword for take information from coordinate
def compare_screen_get_information(
    path1, save_folder="../cs_get_info", folder_csv="../CSV_ERROR"
):

    """	Compare the already save image with the browser screen

    Compares the already saved image with the screen that is on the screen. If there is a difference, it saves the
    highlighted image to the: ../Save Image and making csv file with coordinates and elements which exist on this
    coordinates

    path1 = path to the image to be compared to screen

    Example: Compare screen ../image1.png
    """
    _check_dir(folder_csv)
    _check_dir(save_folder)
    # Making screen
    robotlib = BuiltIn().get_library_instance("BuiltIn")
    seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
    seleniumlib.capture_page_screenshot(save_folder + "/test_screen.png")
    path2 = save_folder + "/test_screen.png"
    if os.path.exists(path1) and os.path.exists(path2):
        # load img
        img1 = cv.imread(path1, 1)
        img2 = cv.imread(path2, 1)

        # convert to grey
        gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        # SSIM diff img
        (score, diff) = structural_similarity(gray_img1, gray_img2, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM: {}".format(score))

        # Threshold diff img
        thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
        cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # write coordinate
        with open(folder_csv + "/bug_coordinates.csv", "w") as csvfile:
            writer = csv.writer(csvfile)
            a = "path", "x_center", "y_center", "x", "y", "x1", "y1"
            writer.writerow(a)

            # Create frame in diff area
            for c in cnts:
                (x, y, w, h) = cv.boundingRect(c)
                cv.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)
                x2 = x + w
                y2 = y + h
                x_center = x + ((x2 - x) / 2)
                y_center = y + ((y2 - y) / 2)
                f = path1, x_center, y_center, x, y, x2, y2
                writer.writerow(f)

        # Save image and show report
        print(score)
        if int(score) < 1.0:
            # TODO: Add screen to log
            img_diff = cv.hconcat([img1, img2])
            cas = str(time.time())
            seleniumlib.capture_page_screenshot(save_folder + "/img{0}.png".format(cas))
            cv.imwrite(save_folder + "/img{0}.png".format(cas), img_diff)

            # start reading coordinates and saving element from coordinate
            df = pd.read_csv(r"" + folder_csv + "/bug_coordinates.csv")
            with open(
                folder_csv + "/bug_co_and_name{0}.csv".format(str(time.time())), "w"
            ) as csv_name:
                writer = csv.writer(csv_name)
                a = "web-page", "x_center", "y_center", "class", "id", "name"
                writer.writerow(a)

                # Get information from position
                for i in range(len(df)):
                    x_center = df.values[i, 1]
                    y_center = df.values[i, 2]
                    driver = seleniumlib.driver
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
            score_percen = float(score) * +100
            print("score" + str(score))
            robotlib.fail("Image has diff: {} %".format(score_percen))
    else:
        print("Bad or not exists path for picture or screen")
