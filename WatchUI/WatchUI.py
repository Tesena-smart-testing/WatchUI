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




watch = WatchUI()
watch.compare_images("C:\Projects\Python\WatchUI\Img\img.png", "C:\Projects\Python\WatchUI\Img\img.png")
