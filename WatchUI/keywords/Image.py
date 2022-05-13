# pylint: disable=invalid-name, expression-not-assigned, unbalanced-tuple-unpacking, too-many-arguments, too-many-locals, no-member
import time
from typing import Any, Optional, Union

from robot.api.deco import keyword
import cv2 as cv
import imutils
from numpy import ndarray
from skimage.metrics import structural_similarity
from ..Ibasic.IBasic import IBasic


class Image(IBasic):
    """Class representing the Image and methods for RF keywords regarding
    comparing the images.
    This class is not instantiated itself.
    Args:
        Basics (object): interface class
    """

    save_folder = ""
    ssim = 1.0
    image_format = "png"

    def _do_checks(self, expected_returned_items: int, **kwargs) -> tuple[Any, ...]:
        keys: list[Any] = list(kwargs.keys())

        checked_save_folder: Optional[str] = (
            self.check_dir(kwargs["save_folder"]) if "save_folder" in keys else None
        )
        ssim: Optional[float] = (
            self.check_ssim(kwargs["ssim"]) if "ssim" in keys else None
        )
        img_format: Optional[str] = (
            self.check_image_format(kwargs["image_format"])
            if "image_format" in keys
            else None
        )
        self.check_image_exists(
            kwargs["base_image_path"]
        ) if "base_image_path" in keys else None
        self.check_image_exists(
            kwargs["compared_image_path"]
        ) if "compared_image_path" in keys else None

        output: list[Union[str, float]] = []
        checked_save_folder is not None and output.append(checked_save_folder)  # type: ignore
        ssim is not None and output.append(ssim)  # type: ignore
        img_format is not None and output.append(img_format)  # type: ignore

        if len(output) != expected_returned_items:
            raise IndexError(
                "Expected items to be returned by the method differs from actual."
            )

        return tuple(output)

    @staticmethod
    def _get_images(base_image_path: str, compared_image_path: str) -> tuple[Any, ...]:
        img1: Any = cv.imread(base_image_path, 1)
        img2: Any = cv.imread(compared_image_path, 1)

        return tuple([img1, img2])

    @staticmethod
    def _convert_to_grey(base_image: Any, target_image: Any) -> tuple[Any, ...]:
        gray_img1: Any = cv.cvtColor(base_image, cv.COLOR_BGR2GRAY)
        gray_img2: Any = cv.cvtColor(target_image, cv.COLOR_BGR2GRAY)

        return tuple([gray_img1, gray_img2])

    @staticmethod
    def _compute_score(
        gray_base_img: Any, gray_targed_img: Any
    ) -> tuple[float, Union[ndarray, Any]]:
        score: float
        diff: Union[ndarray, Any]
        (score, diff) = structural_similarity(gray_base_img, gray_targed_img, full=True)
        diff = (diff * 255).astype("uint8")

        if not isinstance(score, float):
            raise TypeError(
                f"Returned score must be of <float> type. Received {type(score)}"
            )

        return score, diff

    def _write_and_log(
        self,
        score: float,
        ssim: float,
        checked_save_folder: str,
        img_format: str,
        base_image: Any,
        target_image: Any,
    ) -> Any:
        time_: str = str(time.time())
        url: str = f"{checked_save_folder}/Img{time_}{img_format}"
        # Show image
        if score < ssim:
            cv.imwrite(url, target_image)
            self.set_log_message(
                work_object="Image", type_of_messages="Error", path_to_image=url
            )
        else:
            img_diff: Any = cv.hconcat([base_image, target_image])
            cv.imwrite(url, img_diff)
            self.set_log_message(
                work_object="Image", type_of_messages="Info", path_to_image=url
            )

    @staticmethod
    def _get_contours(diff: Union[ndarray, Any]) -> Any:
        thresh: Any = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[
            1
        ]
        cnts: Any = cv.findContours(
            thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )
        return imutils.grab_contours(cnts)

    @keyword
    def compare_images(
        self,
        base_image_path: str,
        compared_image_path: str,
        save_folder=save_folder,
        ssim=ssim,
        image_format=image_format,
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
        checked_save_folder, ssim, img_format = self._do_checks(
            3,
            save_folder=save_folder,
            base_image_path=base_image_path,
            compared_image_path=compared_image_path,
            ssim=ssim,
            image_format=image_format,
        )

        # Compare image
        img1, img2 = self._get_images(base_image_path, compared_image_path)

        # convert to grey
        gray_img1, gray_img2 = self._convert_to_grey(img1, img2)

        # SSIM diff Img
        score, diff = self._compute_score(gray_img1, gray_img2)

        # Threshold diff Img
        cnts: Any = self._get_contours(diff)

        # Create frame in diff area
        for c in cnts:
            (x, y, w, h) = cv.boundingRect(c)
            cv.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

        self._write_and_log(score, ssim, checked_save_folder, img_format, img1, img2)

    @keyword
    def compare_screen_without_areas(
        self,
        base_image_path: str,
        compared_image_path: str,
        *args,
        save_folder=save_folder,
        ssim=ssim,
        image_format=image_format,
    ) -> None:
        """Compares two images without selected areas of the image.
        Args:
            base_image_path (str): path to the base image
            compared_image_path (str): path to the compared image
            save_folder (str): path to the save folder
            ssim (float): SSIM threshold value
            image_format (str): format of the image, e.g. "png", "jpg"
        """
        checked_save_folder, my_ssim, img_format = self._do_checks(
            3,
            save_folder=save_folder,
            base_image_path=base_image_path,
            compared_image_path=compared_image_path,
            ssim=ssim,
            image_format=image_format,
        )

        lt: int = len(args)
        img1, img2 = self._get_images(base_image_path, compared_image_path)

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
        gray_img1, gray_img2 = self._convert_to_grey(img1, img2)

        # SSIM diff Img
        score, diff = self._compute_score(gray_img1, gray_img2)

        # Threshold diff Img
        cnts: Any = self._get_contours(diff)

        # Create frame in diff area
        for c in cnts:
            (x, y, w, h) = cv.boundingRect(c)
            cv.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Show image
        self._write_and_log(score, my_ssim, checked_save_folder, img_format, img1, img2)

    @keyword
    def crop_image(
        self,
        path: str,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        save_folder=save_folder,
        image_format=image_format,
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
        checked_save_folder, img_save_format = self._do_checks(
            2, save_folder=save_folder, image_format=image_format, base_image_path=path
        )

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

    @keyword
    def rotate_image(
        self,
        path: str,
        screen_name="rotate_img",
        angle=0,
        save_folder=save_folder,
        image_format=image_format,
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
        if angle not in [0, 1, 2]:
            raise ValueError(
                "Value of 'rotate' argument can only be of type <Literal[0, 1, 2]>"
            )
        checked_save_folder, img_format = self._do_checks(
            2, save_folder=save_folder, image_format=image_format, base_image_path=path
        )

        img: Any = cv.imread(path)
        save_path: str = f"{checked_save_folder}/{screen_name}{img_format}"
        rotate_image: Any

        if angle == 0:
            rotate_image = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
            return cv.imwrite(save_path, rotate_image)
        if angle == 1:
            rotate_image = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
            return cv.imwrite(save_path, rotate_image)
        if angle == 2:
            rotate_image = cv.rotate(img, cv.ROTATE_180)
            return cv.imwrite(save_path, rotate_image)

        return None
