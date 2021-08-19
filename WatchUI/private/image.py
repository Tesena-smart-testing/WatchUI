'''Class representing the Image object.
'''

from typing import Literal

from WatchUI.interfaces.interface import Interface
from WatchUI.modules.reporting import Reporting


class Image(Interface, Reporting):
    def __init__(
        self,
        ssim_basic: float,
        format_image: Literal["png", "jpg"],
        tesseract_path: str,
        outputs_folder: str,
        path_to_image_1: str,
        path_to_image_2: str,
        path_to_image_3: str,
    ) -> None:
        super().__init__(ssim_basic, format_image, tesseract_path, outputs_folder)
        self.path_to_image_1: str = path_to_image_1
        self.path_to_image_2: str = path_to_image_2
        self.path_to_image_3: str = path_to_image_3

    def compare_images(self):
        pass

    def create_area(self):
        pass

    def rotate_image(self):
        pass

    def create_area_from_image(self):
        pass
