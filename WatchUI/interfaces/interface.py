'''Control interface for private classes.
'''
import os

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

    def _check_dir(self, save_folder):
        """Checks, if given <save_folder> exists, if not, creates it.

        Arguments:
            save_folder {str} -- path to <save_folder>
        """
        if save_folder != self.save_folder_path and save_folder != "":
            if os.path.exists(save_folder):
                self.save_folder = save_folder
            else:
                os.mkdir(save_folder)
                self.save_folder = save_folder
        else:
            if os.path.exists(self.outputs_folder):
                self.save_folder = self.outputs_folder
            else:
                os.mkdir(self.outputs_folder)
                self.save_folder = self.outputs_folder

    def _check_ssim(self, ssim):
        if ssim == 1.0 or ssim == "":
            self.ssim = float(self.ssim_basic)
        else:
            self.ssim = float(ssim)

    def _check_image_format(self, format):
        if str(format) == 'png' or str(format):
            self.format = '.' + self.image_format
        else:
            self.format = '.' + format
