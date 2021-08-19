'''Class representing PDF object.
'''

from typing import Literal

from WatchUI.interfaces.interface import Interface


class Pdf(Interface):
    def __init__(
        self,
        ssim_basic: float,
        format_image: Literal["png", "jpg"],
        tesseract_path: str,
        outputs_folder: str,
        path_to_image: str,
        zoom: float,
    ) -> None:
        super().__init__(ssim_basic, format_image, tesseract_path, outputs_folder)
        self.path_to_image: str = path_to_image
        self.zoom: float = zoom

    def pdf_to_image(self):
        pass

    def return_text_from_area(self):
        pass

    def should_this_text_exist(self):
        pass
