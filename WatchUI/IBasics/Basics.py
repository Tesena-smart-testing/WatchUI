import os


class Basics:
    save_folder_path = "../Outputs"
    ssim_basic = 1.5
    starts_format_image = "png"
    path_to_tesseract_folder = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def check_dir(self, save_folder):
        if save_folder != self.save_folder_path:
            os.mkdir(save_folder)
        return self.save_folder_path

    def check_image_exists(self, path):
        if not os.path.exists(path):
            raise AssertionError("The path: %s, to the image does not exist." % path)

    def check_ssim(self, ssim):
        if ssim == 1.0:
            return float(self.ssim_basic)
        else:
            return float(ssim)

    def check_image_format(self, format):
        if str(format) == 'png':
            self.format = '.' + self.starts_format_image
        else:
            self.format = '.' + format
        return self.format

    def check_tess_path(self, path_to_tess):
        if path_to_tess == r'C:\Program Files\Tesseract-OCR\tesseract.exe':
            tess_way = self.path_to_tesseract_folder
        else:
            tess_way = path_to_tess
        return tess_way
