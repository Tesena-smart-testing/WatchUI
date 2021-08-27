'''Class representing the Tesseract.
'''

from WatchUI.common.types import CustomPath, ImageFormat, Unknown
from WatchUI.interfaces.interface import Interface
from WatchUI.modules.reporting import Reporting


class Tesseract(Interface, Reporting):
    def __init__(
        self,
        ssim_basic: float,
        format_image: ImageFormat,
        tesseract_path: CustomPath,
        outputs_folder: CustomPath,
        path_to_image_1: CustomPath,
        path_to_tesseract: CustomPath,
        oem: Unknown,
        psm: Unknown,
        language: Unknown,
    ) -> None:
        super().__init__(ssim_basic, format_image, tesseract_path, outputs_folder)
        self.path_to_image_1: CustomPath = path_to_image_1
        self.path_to_tesseract: CustomPath = path_to_tesseract
        self.oem: Unknown = oem
        self.psm: Unknown = psm
        self.language: Unknown = language

    def image_to_string(self):
        pass

    def image_area_on_text(self):
        pass
