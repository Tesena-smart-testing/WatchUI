'''Class representing Playwright object, used to perform tasks supported by WatchUI.
'''

from robot.libraries.BuiltIn import BuiltIn
from WatchUI.common.types import CustomPath, ImageFormat
from WatchUI.private.image import Image
from WatchUI.private.pdf import Pdf
from WatchUI.private.tesseract import Tesseract


class Playwright(Image, Pdf, Tesseract):
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
