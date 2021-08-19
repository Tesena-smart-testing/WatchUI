'''Class representing Playwright object, used to perform tasks supported by WatchUI.
Class is inheriting from MarketSquare-Browser robotframework library to keep the implementation
as simple as possible and compatible. MarketSquare-Browser is also probably most used playwright library for RF
'''
from typing import Literal

from private.image import Image
from private.pdf import Pdf
from private.tesseract import Tesseract

from robot.libraries.BuiltIn import BuiltIn


class Playwright:
    def __init__(
        self,
        ssim_basic: float,
        format_image: Literal["png", "jpg"],
        tesseract_path: str,
        outputs_folder: str,
    ) -> None:
        self.browser = BuiltIn().get_library_instance("browser")
        self.image = Image(
            ssim_basic=ssim_basic,
            format_image=format_image,
            tesseract_path=tesseract_path,
            outputs_folder=outputs_folder,
        )
        self.pdf = Pdf(
            ssim_basic=ssim_basic,
            format_image=format_image,
            tesseract_path=tesseract_path,
            outputs_folder=outputs_folder,
        )
        self.tesseract = Tesseract(
            ssim_basic=ssim_basic,
            format_image=format_image,
            tesseract_path=tesseract_path,
            outputs_folder=outputs_folder,
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
