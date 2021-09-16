from WatchUI.Keywords.Image import Image


class WatchUI(Image):
    save_folder_path = "../Outputs"
    starts_ssim = 1.0
    starts_format_image = "png"
    path_to_tesseract_folder = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def __init__(self, outputs_folder=save_folder_path, ssim_basic=starts_ssim, format_image=starts_format_image,
                 tesseract_path=path_to_tesseract_folder):
        self.outputs_folder = outputs_folder
        self.ssim_basic = float(ssim_basic)
        self.image_format = str(format_image)
        self.tesseract_path = str(tesseract_path)

    def compare_image(self, path1, path2, save_folder=save_folder_path, ssim=starts_ssim, image_format=starts_format_image):
        self.compare_images(self, path1, path2, save_folder, ssim, image_format)

    def compare_screen_without_areas(self, path1, path2, *args, save_folder=save_folder_path, ssim=starts_ssim, image_format=starts_format_image):
        self.create_compare_screen_without_areas(self, path1, path2, *args, save_folder, ssim, image_format)

    def crop_image(self, path, x1, x2, y1, y2, save_folder=save_folder_path, image_format=starts_format_image):
        self.create_crop_image(path, x1, x2, y1, y2, save_folder, image_format)

    def rotate_image(self, path, screen_name="rotate_screen",
                     save_folder=save_folder_path,
                     rotate=0,
                     image_format=starts_format_image):
        self.create_crop_image(self, path, screen_name, save_folder, rotate, image_format)

