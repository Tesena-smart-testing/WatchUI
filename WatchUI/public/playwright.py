'''Class representing Playwright object, used to perform tasks supported by WatchUI.
'''

from robot.libraries.BuiltIn import BuiltIn
from WatchUI.common.types import CustomPath, ImageFormat
from WatchUI.private.image import Image
from WatchUI.private.pdf import Pdf
from WatchUI.private.tesseract import Tesseract


class Playwright(Image, Pdf, Tesseract):
    """Class representing Playwright RF library instance.

    Args:
        Image (Image): Image class inherited
        Pdf (Pdf): Pdf class inherited
        Tesseract (Tesseract): Tesseract class inherited
    """

    def __init__(
        self,
        ssim_basic: float,
        format_image: ImageFormat,
        tesseract_path: CustomPath,
        outputs_folder: CustomPath,
        path_to_image_1: CustomPath,
        path_to_image_2: CustomPath,
        path_to_image_3: CustomPath,
    ) -> None:
        """Initalizes the instance of the Playwright class.

        Args:
            ssim_basic (float): basic SSIM threshold value
            format_image (ImageFormat): format of the screenshots
            tesseract_path (CustomPath): path to tesseract
            outputs_folder (CustomPath): path to test run outputs
            path_to_image_1 (CustomPath): path to image 1
            path_to_image_2 (CustomPath): path to image 2
            path_to_image_3 (CustomPath): path to image 3
        """
        super().__init__(
            ssim_basic=ssim_basic,
            format_image=format_image,
            tesseract_path=tesseract_path,
            outputs_folder=outputs_folder,
            path_to_image_1=path_to_image_1,
            path_to_image_2=path_to_image_2,
            path_to_image_3=path_to_image_3,
        )
        self.browser = BuiltIn().get_library_instance("browser")

    def _take_screenshot(
        self,
        filepath: str,
        fullpage: bool = False,
        filetype: ImageFormat = "jpeg",
        **kwargs,
    ):
        """Takes screenshot using Playwright RF Browser library instance method.

        Args:
            filepath (str): filename or filepath to where screenshot should be saved.
            fullPage (bool, optional): Full page or viewport screenshot?. Defaults to False.
            filetype (ImageFormat, optional): Type of screenshot file format. Defaults to "png".
        """
        self.browser.take_screenshot(
            filename=filepath, fullPage=fullpage, fileType=filetype, **kwargs
        )

    def compare_screen(self):
        pass

    def create_area(self):
        pass

    def create_screens(self):
        pass

    def compare_screen_areas(self):
        pass

    def compare_screen_without_areas(self):
        pass

    def compare_screen_compare_screen_get_information(self):
        pass
