'''Class representing PDF object.
'''

from WatchUI.common.types import CustomPath, ImageFormat
from WatchUI.interfaces.interface import Interface
from WatchUI.modules.reporting import Reporting


class Pdf(Interface, Reporting):
    def __init__(
        self,
        ssim_basic: float,
        format_image: ImageFormat,
        tesseract_path: CustomPath,
        outputs_folder: CustomPath,
        path_to_image: CustomPath,
        zoom: float,
    ) -> None:
        super().__init__(ssim_basic, format_image, tesseract_path, outputs_folder)
        self.path_to_image: CustomPath = path_to_image
        self.zoom: float = zoom

    def pdf_to_image(self):
        pass

    def return_text_from_area(self):
        pass

    def should_this_text_exist(self):
        pass
