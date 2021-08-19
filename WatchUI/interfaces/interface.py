'''Control interface for private classes.
'''

from typing import Literal


class Interface:
    def __init__(
        self,
        ssim_basic: float,
        format_image: Literal["png", "jpg"],
        tesseract_path: str,
        outputs_folder: str,
    ) -> None:
        self.ssim_basic: float = ssim_basic
        self.format_image: Literal["png", "jpg"] = format_image
        self.tesseract_path: str = tesseract_path
        self.outputs_folder: str = outputs_folder

    def _check_dir(self):
        pass

    def _check_ssim(self):
        pass

    def _check_image_format(self):
        pass
