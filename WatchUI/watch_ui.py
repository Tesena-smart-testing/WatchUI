'''Class representing RobotFramework WatchUI library.
'''

from typing import Literal

from robot.api.deco import keyword, library

from WatchUI.public.playwright import Playwright
from WatchUI.public.selenium import Selenium


@library(scope="module")
class WatchUI:
    def __init__(
        self,
        rf_library: Literal["selenium", "playwright"],
        ssim_basic: float,
        format_image: Literal["png", "jpg"],
        tesseract_path: str,
        outputs_folder: str,
        path_to_image_1: str,
        path_to_image_2: str,
        path_to_image_3: str,
    ) -> None:

        self.ssim_basic = ssim_basic
        self.format_image = format_image
        self.tesseract_path = tesseract_path
        self.outputs_folder = outputs_folder
        self.path_to_image_1 = path_to_image_1
        self.path_to_image_2 = path_to_image_2
        self.path_to_image_3 = path_to_image_3
        self.rf_library = self._instantiate(rf_library)

    def _instantiate(self, rf_library: Literal["selenium", "playwright"]):
        if rf_library == "selenium":
            return Selenium(
                self.ssim_basic,
                self.format_image,
                self.tesseract_path,
                self.outputs_folder,
                self.path_to_image_1,
                self.path_to_image_2,
                self.path_to_image_3,
            )

        if rf_library == "playwright":
            return Playwright(
                self.ssim_basic,
                self.format_image,
                self.tesseract_path,
                self.outputs_folder,
                self.path_to_image_1,
                self.path_to_image_2,
                self.path_to_image_3,
            )

        raise RuntimeError("'selenium' or 'playwright' libraries are supported.")

    @keyword
    def compare_screen(self):
        self.rf_library.compare_screen()

    @keyword
    def create_area(self):
        self.rf_library.create_area()

    @keyword
    def create_screens(self):
        self.rf_library.create_screens()

    @keyword
    def compare_screen_areas(self):
        self.rf_library.compare_screen_areas()

    @keyword
    def compare_screen_without_areas(self):
        self.rf_library.compare_screen_without_areas()

    @keyword
    def compare_screen_compare_screen_get_information(self):
        self.rf_library.compare_screen_compare_screen_get_information()
