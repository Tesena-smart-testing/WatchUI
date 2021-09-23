# pylint: disable=invalid-name

"""Image class module.
"""
# pylint: disable=no-member
import time
from typing import Any, Literal, Union

import cv2 as cv
import imutils
from numpy import ndarray
from skimage.metrics import structural_similarity
from WatchUI.IBasics.Basics import Basics


class Image(Basics):
    """Class representing the Image and methods for RF keywords regarding
    comparing the images.

    This class is not instantiated itself.

    Args:
        Basics (object): interface class
    """

    def create_compare_images(
        self,
        base_image_path: str,
        compared_image_path: str,
        save_folder: str,
        ssim: float,
        image_format: str,
    ) -> None:
        """Compares image on `compared_image_path` against base image on `base_image_path`.

        Args:
            base_image_path (str): path to base image
            compared_image_path (str): path to compared image
            save_folder (str): path to the save folder
            ssim (float): SSIM threshold value
            image_format (str): image format, e.g. "png", "jpg"

        Raises:
            TypeError:
        """
        save_folder = self.check_dir(save_folder)
        ssim = self.check_ssim(ssim)
        img_format = self.check_image_format(image_format)
        self.check_image_exists(base_image_path)
        self.check_image_exists(compared_image_path)

        # Compare image
        img1: Any = cv.imread(base_image_path, 1)
        img2: Any = cv.imread(compared_image_path, 1)

        # convert to grey
        gray_img1: Any = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        gray_img2: Any = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        # SSIM diff Img
        score: float
        diff: Union[ndarray, Any]
        (score, diff) = structural_similarity(gray_img1, gray_img2, full=True)
        diff = (diff * 255).astype("uint8")
        score = float(score)

        if not isinstance(score, float):
            raise TypeError(
                f"Returned score must be of <float> type. Received {type(score)}"
            )

        # Threshold diff Img
        thresh: Any = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[
            1
        ]
        cnts: Any = cv.findContours(
            thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )
        cnts = imutils.grab_contours(cnts)

        # Create frame in diff area
        for c in cnts:
            (x, y, w, h) = cv.boundingRect(c)
            cv.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

        time_: str = str(time.time())
        url: str = f"{save_folder}/Img{time_}{img_format}"
        # Show image
        if score < ssim:
            cv.imwrite(url, img2)
            self.set_log_message(
                work_object="Image", type_of_messages="Error", path_to_image=url
            )
        else:
            img_diff: Any = cv.hconcat([img1, img2])
            cv.imwrite(url, img_diff)
            self.set_log_message(
                work_object="Image", type_of_messages="Info", path_to_image=url
            )

    def create_compare_screen_without_areas(
        self,
        base_image_path: str,
        compared_image_path: str,
        *args,
        save_folder: str,
        ssim: float,
        image_format: str,
    ) -> None:
        """Compares two images without selected areas of the image.

        Args:
            base_image_path (str): path to the base image
            compared_image_path (str): path to the compared image
            save_folder (str): path to the save folder
            ssim (float): SSIM threshold value
            image_format (str): format of the image, e.g. "png", "jpg"
        """
        checked_save_folder: str = self.check_dir(save_folder)
        my_ssim: float = self.check_ssim(ssim)
        img_format: str = self.check_image_format(image_format)

        lt: int = len(args)
        img1: Any = cv.imread(base_image_path, 1)
        img2: Any = cv.imread(compared_image_path, 1)

        self.check_if_args_has_ok_numbers(*args, need_numbers=4)

        x: float = lt / 4
        i: int = 0
        a: int = 0
        while i < x:
            color: tuple[int, int, int] = (0, 0, 0)
            x1: int = int(args[0 + a])
            y1: int = int(args[1 + a])
            x2: int = int(args[2 + a])
            y2: int = int(args[3 + a])

            cv.rectangle(img1, (x1, y1), (x2, y2), color, -1)
            cv.rectangle(img2, (x1, y1), (x2, y2), color, -1)
            a += 4
            i += 1

            # convert to grey
            gray_img1: Any = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
            gray_img2: Any = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

            # SSIM diff Img
            score: float
            diff: Union[Any, ndarray]
            (score, diff) = structural_similarity(gray_img1, gray_img2, full=True)
            diff = (diff * 255).astype("uint8")
            score = float(score)

            # Threshold diff Img
            thresh: Any = cv.threshold(
                diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU
            )[1]
            cnts: Any = cv.findContours(
                thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
            )
            cnts = imutils.grab_contours(cnts)

            # Create frame in diff area
            for c in cnts:
                (x, y, w, h) = cv.boundingRect(c)
                cv.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Show image
            time_: str = str(time.time())
            url: str = f"{checked_save_folder}/Img{time_}{img_format}"
            if score < my_ssim:
                cv.imwrite(url, img2)
                self.set_log_message(
                    work_object="Image", type_of_messages="Error", path_to_image=url
                )
            else:
                img_diff = cv.hconcat([img1, img2])
                cv.imwrite(url, img_diff)
                self.set_log_message(
                    work_object="Image", type_of_messages="Info", path_to_image=url
                )

    def create_crop_image(
        self,
        path: str,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        save_folder: str,
        image_format: str,
    ) -> None:
        """Creates cropped image and saves it.

        Args:
            path (str): path to the image
            x1 (int): x1 coords
            y1 (int): y1 coords
            x2 (int): x2 coords
            y2 (int): y2 coords
            save_folder (str): path to save folder
            image_format (str): format of the saved image, e.g. "png", "jpg"
        """
        self.check_image_exists(path)
        checked_save_folder: str = self.check_dir(save_folder)
        img_save_format: str = self.check_image_format(image_format)

        img: Any = cv.imread(path, 1)
        crop_img: Any = img[
            int(x1) : int(x2), int(y1) : int(y2)
        ]  # Crop from {x, y, w, h } => {0, 0, 300, 400}

        # Save image
        url: str = f"{checked_save_folder}/Img{str(time.time())}{img_save_format}"
        cv.imwrite(url, crop_img)
        self.set_log_message(
            work_object="Image", type_of_messages="Info", path_to_image=url
        )

    def create_rotate_image(
        self,
        path: str,
        screen_name: str,
        save_folder: str,
        rotate: Literal[0, 1, 2],
        image_format: str,
    ) -> Any:
        """Creates rotated version of the source image and saves it.

        Args:
            path (str): path to the source image
            screen_name (str): name of the screen
            save_folder (str): path to the save folder
            rotate (int): [description]
            image_format (str): [description]

        Raises:
            AssertionError: [description]
        """
        if rotate not in [0, 1, 2]:
            raise ValueError(
                "Value of 'rotate' argument can only be of type <Literal[0, 1, 2]>"
            )

        checked_save_folder: str = self.check_dir(save_folder)
        img_format: str = self.check_image_format(image_format)
        self.check_image_exists(path)

        img: Any = cv.imread(path)
        save_path: str = f"{checked_save_folder}/{screen_name}{img_format}"
        rotate_image: Any

        if rotate == 0:
            rotate_image = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
            return cv.imwrite(save_path, rotate_image)
        if rotate == 1:
            rotate_image = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
            return cv.imwrite(save_path, rotate_image)
        if rotate == 2:
            rotate_image = cv.rotate(img, cv.ROTATE_180)
            return cv.imwrite(save_path, rotate_image)

        return None
