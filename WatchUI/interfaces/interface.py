'''Control interface for private classes.
'''

from WatchUI.common.types import CustomPath, ImageFormat


class Interface:
    def __init__(
        self,
        ssim_basic: float,
        format_image: ImageFormat,
        tesseract_path: CustomPath,
        outputs_folder: CustomPath,
    ) -> None:
        self.ssim_basic: float = ssim_basic
        self.format_image: ImageFormat = format_image
        self.tesseract_path: CustomPath = tesseract_path
        self.outputs_folder: CustomPath = outputs_folder

    def _check_dir(self):
        pass

    def _check_ssim(self):
        pass

    def _check_image_format(self):
        pass
