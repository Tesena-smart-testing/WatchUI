'''Class representing the Tesseract.
'''

from typing import Any, Literal

from WatchUI.interfaces.interface import Interface
from WatchUI.modules.reporting import Reporting


class Tesseract(Interface, Reporting):
    def __init__(
        self,
        ssim_basic: float,
        format_image: Literal["png", "jpg"],
        tesseract_path: str,
        outputs_folder: str,
        path_to_image_1: str,
        path_to_tesseract: str,
        oem: Any,
        psm: Any,
        language: Any,
    ) -> None:
        super().__init__(ssim_basic, format_image, tesseract_path, outputs_folder)
        self.path_to_image_1: str = path_to_image_1
        self.path_to_tesseract: str = path_to_tesseract
        self.oem: Any = oem
        self.psm: Any = psm
        self.language: Any = language

    def image_to_string(self):
        pass

    def image_area_on_text(self):
        pass
