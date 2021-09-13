import os

class Basics:
    save_folder_path = "../Outputs"
    starts_ssim = 1.0
    starts_format_image = "png"
    path_to_tesseract_folder = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def __init__(self, outputs_folder=save_folder_path, ssim_basic=starts_ssim, format_image=starts_format_image, tesseract_path=path_to_tesseract_folder):
        self.outputs_folder = outputs_folder
        self.ssim_basic = float(ssim_basic)
        self.image_format = str(format_image)
        self.tesseract_path = str(tesseract_path)

    def check_dir(self, save_folder):
        if save_folder != self.save_folder_path:
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

    def check_image_exists(self, path):
        if not os.path.exists(path):
            raise AssertionError("The path: %s, to the image does not exist." % path)

    def check_ssim(self, ssim):
        if ssim == 1.0:
            self.ssim = float(self.ssim_basic)
        else:
            self.ssim = float(ssim)

    def check_image_format(self, format):
        if str(format) == 'png':
            self.format = '.' + self.image_format
        else:
            self.format = '.' + format

    def check_tess_path(self, path_to_tess):
        if path_to_tess == r'C:\Program Files\Tesseract-OCR\tesseract.exe':
            self.tess_way = self.tesseract_path
        else:
            self.tess_way = path_to_tess