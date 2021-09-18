import os

from robot.api import logger


class Basics:
    save_folder_path = "../Outputs"
    ssim_basic = float(1.0)
    starts_format_image = "png"
    path_to_tesseract_folder = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    def check_dir(self, save_folder: str) -> str:
        if save_folder != self.save_folder_path:
            self.save_folder_path = save_folder

        if not os.path.exists(self.save_folder_path):
            os.mkdir(self.save_folder_path)

        return self.save_folder_path

    @staticmethod
    def check_image_exists(path: str) -> None:
        if not os.path.exists(path):
            raise AssertionError("The path: %s, to the image does not exist." % path)

    def check_ssim(self, ssim: float) -> float:
        if ssim == self.ssim_basic:
            return self.ssim_basic
        return float(ssim)

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

    def check_tess_path(self, path_to_tess: str) -> str:
        if path_to_tess == r"C:\Program Files\Tesseract-OCR\tesseract.exe":
            tess_way = self.path_to_tesseract_folder
        else:
            tess_way = path_to_tess
        return tess_way

    @staticmethod
    def set_log_message(work_object="Image", type_of_messages="Info", path_to_image=""):
        if work_object == "Image":
            if type_of_messages == "Info":
                logger.info(
                    "Image was saved to your output folder </p><img src='"
                    + path_to_image
                    + "'/>",
                    html=True,
                )
            elif type_of_messages == "Error":
                logger.error(
                    "Images arent same</p><img src='" + path_to_image + "'/>", html=True
                )
                raise AssertionError("Images arent same")
        elif work_object == "PDF":
            pass
        elif work_object == "Tesseract":
            pass
        else:
            logger.warn(
                "!!! Bad work object !!! Please contact library owner...", html=True
            )

    @staticmethod
    def check_if_args_has_ok_numbers(*args, need_numbers=4):
        n_arg = len(args)
        logger.info(args)
        if n_arg % need_numbers == 0:
            True
        else:
            logger.error(
                "You try to set bad numbers of arguments. You need %s arguments"
                % need_numbers,
                html=False,
            )
            raise AssertionError(
                "You try to set bad numbers of arguments. You need %s arguments"
                % need_numbers
            )
