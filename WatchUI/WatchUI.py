from WatchUI.Keywords.Image import Image
from WatchUI.Keywords.PDF import Pdf
from WatchUI.Keywords.Tesseract import Tesseract


class WatchUI(Image, Pdf, Tesseract):
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

    def compare_image(self, path1, path2, save_folder=save_folder_path, ssim=starts_ssim, image_format=starts_format_image) -> None:
        self.create_compare_images(path1=path1, path2=path2, save_folder=save_folder, ssim=ssim, image_format=image_format)

    def compare_screen_without_areas(self, path1, path2, *args, save_folder=save_folder_path, ssim=starts_ssim, image_format=starts_format_image) -> None:
        self.create_compare_screen_without_areas(path1, path2, *args, save_folder=save_folder, ssim=ssim, image_format=image_format)

    def crop_image(self, path, x1: int, y1: int, x2: int, y2: int, save_folder=save_folder_path, image_format=starts_format_image) -> None:
        self.create_crop_image(path=path, x1=x1, y1=y1, x2=x2, y2=y2, save_folder=save_folder, image_format=image_format)

    def rotate_image(self, path, screen_name="img",
                     save_folder=save_folder_path,
                     rotate=0,
                     image_format=starts_format_image) -> None:
        self.create_rotate_image(path=path, screen_name=screen_name, save_folder=save_folder, rotate=rotate, image_format=image_format)

    def pdf_to_image(self, path, save_folder=save_folder_path, screen_name="pdf_screen", number_page="-1") -> None:
        self.create_pdf_to_image(path=path, save_folder=save_folder, name=screen_name, number_page=number_page)

    def return_text_from_area(self, path, page_number: int, x1: int, y1: int, x2: int, y2: int) -> str:
        return self.create_return_text_from_area(path=path, page_number=page_number, x1=x1, y1=y1, x2=x2, y2=y2)

    def should_exist_this_text(self, path, page_number: int, text: str) -> bool:
        return self.create_should_exist_this_text(path=path, page_number=page_number, text=text)

    def image_to_string(self, path, oem="3", psm="3", language="eng", path_to_tesseract=path_to_tesseract_folder) -> str:
        return self.create_image_to_string(path=path, oem=oem, psm=psm, language=language, path_to_tesseract=path_to_tesseract)

    def image_area_on_text(self, path, *coordinates, oem='3', psm='3', language='eng',
                           path_to_tesseract=path_to_tesseract_folder) -> str:
        return self.create_image_area_on_text(path, *coordinates, oem=oem, psm=psm, language=language, path_to_tesseract=path_to_tesseract)