# pylint: disable=invalid-name
"""
Basics class
"""
import os
from typing import Literal
from robot.api import logger
from robot.api.deco import not_keyword


class IBasic:
    """
    Interface to be inherited by Classes implementing keyword methods.
    Raises:
        FileExistsError:
        TypeError:
        ValueError:
        AssertionError:
        ValueError:
    """

    def __init__(self, save_folder_path, ssim, format_image, tesseract_path) -> None:
        self.save_folder_path = save_folder_path
        self.ssim_basic = ssim
        self.starts_format_image = format_image
        self.path_to_tesseract_folder = tesseract_path

    @not_keyword
    def check_dir(self, save_folder: str) -> str:
        """Checks given value for `save_folder`, verifies against default and if it
        does not exists, creates it.
        Args:
            save_folder (str): path to save folder
        Returns:
            str: self.save_folder_path
        """
        if save_folder != "":
            self.save_folder_path = save_folder

        if not os.path.exists(self.save_folder_path):
            os.mkdir(self.save_folder_path)

        return self.save_folder_path

    @not_keyword
    @staticmethod
    def check_image_exists(path: str) -> None:
        """Checks, that image file on given `path` exists.
        Args:
            path (str): path to given image file.
        Raises:
            FileExistsError:
        """
        if not os.path.exists(path):
            raise FileExistsError(f"The path: {path}, to the image does not exist.")

    @not_keyword
    def check_ssim(self, ssim: float) -> float:
        """Checks, if `ssim` is of `<float>` type and if it is within <0.0 , 1.0> range.
        Args:
            ssim (float): SSIM value
        Raises:
            TypeError:
            ValueError:
        Returns:
            float: returns the SSIM value
        """
        if not isinstance(ssim, float):
            raise TypeError(
                f"'ssim' argument must of type <float>. Provided value is of type {type(ssim)}"
            )
        if (ssim < 0.0) or (ssim > 1.0):
            raise ValueError(
                f"'ssim' value must be in <0.0 , 1.0> inclusive range. You have provided {ssim}"
            )

        if ssim != 1.0:
            self.ssim_basic = ssim
        return self.ssim_basic

    @not_keyword
    def check_image_format(self, image_format: str) -> str:
        """Checks image format. If "png", returns default, else returns `image_format`.
        Args:
            image_format (str): format of the image, e.g. "png", "jpg", etc.
        Returns:
            str: image format file extension, e.g ".png", ".jpg"
        """
        if str(image_format) == "png":
            return f".{self.starts_format_image}"
        return f".{image_format}"

    @not_keyword
    def check_tess_path(self, path_to_tess: str) -> str:
        """Checks, whether `path_to tess` is equal to expected default. If so,
        returns default value.
        Else returns provided value.
        Args:
            path_to_tess (str): path to tesseract folder
        Returns:
            str: self.path_to_tesseract_folder
        """

        if path_to_tess != "":
            self.path_to_tesseract_folder = path_to_tess
        return self.path_to_tesseract_folder

    @not_keyword
    @staticmethod
    def set_log_message(
        work_object: Literal["Image", "PDF", "Tesseract"] = "Image",
        type_of_messages: Literal["Info", "Error"] = "Info",
        path_to_image: str = "",
    ) -> None:
        """Sets logging message.
        Args:
            work_object (Literal[, optional): What object are we working on. Defaults to "Image".
            type_of_messages (Literal[, optional): Type of logging message. Defaults to "Info".
            path_to_image (str, optional): Path to image to be appended to log message.
            Defaults to "".
        Raises:
            AssertionError:
        """
        if work_object == "Image":
            if type_of_messages == "Info":
                logger.info(
                    f"<p>Image was saved to your output folder </p><img src={path_to_image}></img>",
                    html=True,
                )
            elif type_of_messages == "Error":
                logger.error(
                    f"<p>Images arent same</p><img src={path_to_image}></img>",
                    html=True,
                )
                raise AssertionError("Images are not the same")
        elif work_object == "PDF":
            pass
        elif work_object == "Tesseract":
            pass
        else:
            logger.warn(
                "!!! Bad work object !!! Please contact library owner...", html=True
            )

    @not_keyword
    @staticmethod
    def check_if_args_has_ok_numbers(*args, need_numbers: int = 4) -> bool:
        """Verifies, whether correct number of arguments was provided.
        *Args:
            Arguments to be verified
        Args:
            need_numbers (int, optional): required number of arguments. Defaults to 4.
        Raises:
            ValueError:
        Returns:
            bool: True, if number of `*args` matches the `need_number` value.
            Else throws `ValueError`
        """
        n_arg = len(args)
        logger.info(args)
        if n_arg % need_numbers == 0:
            return True

        logger.error(
            f"You tried to set bad numbers of arguments. You need {need_numbers} arguments",
            html=False,
        )
        raise ValueError(
            f"You tried to set bad numbers of arguments. You need {need_numbers} arguments"
        )
