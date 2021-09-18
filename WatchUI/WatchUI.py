from WatchUI.Keywords.Image import Image
from WatchUI.Keywords.PDF import Pdf
from WatchUI.Keywords.Tesseract import Tesseract


class WatchUI(Image, Pdf, Tesseract):
    """WatchUI - Custom library for comparing images with use in Robot Framework.

    = Table of Contents =

    - `Usage`
    - `Importing`
    - `Examples`
    - `Keywords`

    = Usage =

    This library allows for automated visual testing of web frontends.
    Currently, this library is not officialy supported, so best way is to
    clone the repository and copy the WatchUI.py library file into your project and then
    import it - see Importing section.

    However, you can also install it via command *pip install WatchUI* and then import it.

    *IMPORTANT*: When using keywords of this library, please remember, that screenshots have to have same resolution!

    = Examples =
    Import library
    | `Library` | <path_to_library file> | outputs_folder= | ssim_basic= | starts_format_image= |

    Compare Images
    | Compare Images | path1 | path2 | save_folder= | ssim= | starts_format_image= |

    """

    save_folder_path = "../Outputs"
    starts_ssim = 1.0
    starts_format_image = "png"
    path_to_tesseract_folder = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    def __init__(
        self,
        outputs_folder=save_folder_path,
        ssim_basic=starts_ssim,
        format_image=starts_format_image,
        tesseract_path=path_to_tesseract_folder,
    ):
        """Library can be imported either with default output folder and set lowest limit of difference between images (ssim), or
        you can provide your own values.

        Keyword Arguments:

            outputs_folder {str} -- path, where you want to save images with highlighted differences (default: "../Outputs")

            ssim_basic {float} -- threshold value in the interval (0, 1>. Tests are passed, if ssim value returned by keyword test functions is bigger than this (default: 1.0)

            format_image {str} -- Format for saving picture/screenshot (png, jpg etc.) Example: format_image=jpg (default: png)

        Examples:

        | =Setting= | =Value= | =Value= | =Value= | =Comment= |
        | Library   | WatchUI |      |  | # Uses default values of keyword arguments |
        | Library   | WatchUI | outputs_folder=<path_to_folder> | | # changes folder to different one |
        | Library   | WatchUI | outputs_folder=<path_to_folder> | ssim_basic=<float> | # changes output folder and ssim threshold |

        """
        self.outputs_folder = outputs_folder
        self.ssim_basic = float(ssim_basic)
        self.image_format = str(format_image)
        self.tesseract_path = str(tesseract_path)

    def compare_image(
        self,
        path1,
        path2,
        save_folder=save_folder_path,
        ssim=starts_ssim,
        image_format=starts_format_image,
    ) -> None:
        """Comparing images

        It compares two images from the two paths and, if there are differences, saves the image with the errors highlighted
        in the folder: ../Save Image

        path1 = path to the first image to be compared
        path2 = path to the second image to be compared

        Example: Compare two image ../image1.png ../Image2.png
        """
        self.create_compare_images(
            base_image_path=path1,
            compared_image_path=path2,
            save_folder=save_folder,
            ssim=ssim,
            image_format=image_format,
        )

    def compare_screen_without_areas(
        self,
        path1,
        path2,
        *args,
        save_folder=save_folder_path,
        ssim=starts_ssim,
        image_format=starts_format_image
    ) -> None:
        """
        Compares two pictures, which have parts to be ignored
        x1 and y1 = x and y coordinates for the upper left corner of the ignored area square
        x2 and y2 = x and y coordinates for the lower right corner of the square of the ignored part

        Attention! It is always necessary to enter in order x1 y1 x2 y2 x1 y1 x2 y2 etc ...

        Compare screen without areas ../Image1.png 0 0 30 40 50 50 100 100
        Creates 2 ignored parts at 0,0, 30,40 and 50, 50, 100, 100
        """
        self.create_compare_screen_without_areas(
            path1,
            path2,
            *args,
            save_folder=save_folder,
            ssim=ssim,
            image_format=image_format
        )

    def crop_image(
        self,
        path,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        save_folder=save_folder_path,
        image_format=starts_format_image,
    ) -> None:
        self.create_crop_image(
            path=path,
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            save_folder=save_folder,
            image_format=image_format,
        )

    def rotate_image(
        self,
        path,
        screen_name="img",
        save_folder=save_folder_path,
        rotate=0,
        image_format=starts_format_image,
    ) -> None:
        """

        path = Path to the image, which we wanna rotate.
        rotate = How we want to rotate the image. 0 = 90degrees Clockwise, 1 = 90degrees Counter clockwise,
        2= 180degrees
        number_page = PDF page number, which we change into image.

        """
        self.create_rotate_image(
            path=path,
            screen_name=screen_name,
            save_folder=save_folder,
            rotate=rotate,
            image_format=image_format,
        )

    def pdf_to_image(
        self,
        path,
        save_folder=save_folder_path,
        screen_name="pdf_screen",
        number_page="-1",
    ) -> None:
        """
        Change PDF to Image.

        path = Path to the pdf, which we wanna change to image.
        name = Name of the image, we going to creating.
        number_page = PDF page number, which we change into image.

        """
        self.create_pdf_to_image(
            path=path,
            save_folder=save_folder,
            name=screen_name,
            number_page=number_page,
        )

    def return_text_from_area(
        self, path, page_number: int, x1: int, y1: int, x2: int, y2: int
    ) -> str:
        """
        Return text from area. It doesnt use tesseract, so its can be used on normally pdf or without installed
        tesseract
        path = Path to pdf
        page_number = PDF page number where we wanna search for text
        x1, y1, x2, y2 = coordinates where text is
        """
        return self.create_return_text_from_area(
            path=path, page_number=page_number, x1=x1, y1=y1, x2=x2, y2=y2
        )

    def should_exist_this_text(self, path, page_number: int, text: str) -> bool:
        """
        Returns True if <text> is found in page
        path = Path to pdf
        page_number = PDF page number where we wanna check text
        text = Text which we search

        """
        return self.create_should_exist_this_text(
            path=path, page_number=page_number, text=text
        )

    def image_to_string(
        self,
        path,
        oem="3",
        psm="3",
        language="eng",
        path_to_tesseract=path_to_tesseract_folder,
    ) -> str:
        """
        Keyword for reading text from image. For proper functionality you must install tesseract-ocr.

        path = path to the image, which we wanna read
        oem = Engine Mode (Settings from tesseract)
        PSM = Page Segmentation Mode (Settings from tesseract)
        language = The Language we wanna read file
        path_to_tesseract = Path to root folder with tesseract.exe
        """
        return self.create_image_to_string(
            path=path,
            oem=oem,
            psm=psm,
            language=language,
            path_to_tesseract=path_to_tesseract,
        )

    def image_area_on_text(
        self,
        path,
        *coordinates,
        oem="3",
        psm="3",
        language="eng",
        path_to_tesseract=path_to_tesseract_folder
    ) -> str:
        """
        Keyword for reading text from image. For proper functionality you must install tesseract-ocr.

        path = path to the image, which we wanna read
        *coordinates = coordinates where text is located. Must be 4 (x1, y1, x2, y2)
        oem = Engine Mode (Settings from tesseract)
        PSM = Page Segmentation Mode (Settings from tesseract)
        language = The Language we wanna read file
        path_to_tesseract = Path to root folder with tesseract.exe

        """
        return self.create_image_area_on_text(
            path,
            *coordinates,
            oem=oem,
            psm=psm,
            language=language,
            path_to_tesseract=path_to_tesseract
        )
