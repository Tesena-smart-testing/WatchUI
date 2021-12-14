# pylint: disable=invalid-name, line-too-long, too-many-arguments

"""Library module.
"""
from typing import Union

from robot.api.deco import keyword, library

from WatchUI.Keywords.Image import Image
from WatchUI.Keywords.PDF import Pdf
from WatchUI.Keywords.Tesseract import Tesseract


@library
class WatchUI(Image, Pdf, Tesseract):
    """
    
    WatchUI - Robot Framework library for visual validation and testing.

    = Table of Contents =

    - `Usage`
    - `Importing`
    - `Examples`
    - `Keywords`

    = Usage =

    This library provides visual testing automation capabilities for web frontends, UI applications and any other tests where visual testing is required.

    Library can be installed via command `pip install WatchUI`.

    For usage exmaples check out aout GitHub repository: folder examples.

    *Note*: To achieve proper testing results all validated images have to have same resolution.

    = Examples =
    Import library
    | `Library` | <path_to_library file> | outputs_folder= | ssim_basic= | starts_format_image= | tesseract_path= |

    Compare Image
    | Compare Images | login_baseline.png | login_new.png | save_folder="/tmp" | ssim=0.8 | starts_format_image="jpg" |

    """

    default_output_folder = "./outputs"
    default_ssim = 1.0
    default_format_image = "png"
    default_path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    ROBOT_LIBRARY_VERSION = '2.0'

    def __init__(
        self,
        outputs_folder=default_output_folder,
        ssim_basic=default_ssim,
        format_image=default_format_image,
        tesseract_path=default_path_to_tesseract,
    ):
        """Library can be imported either with default output folder and set
        highest limit of difference between images (ssim), or
        you can provide your own values.

        Keyword Arguments:

            outputs_folder {str} -- path, where you want to save images with highlighted
            differences

            ssim {float} -- threshold value in the interval (0, 1>. Tests pass, if ssim value returned by keyword is bigger than ssimm
    
            format_image {str} -- Format for saving picture/screenshot (png, jpg etc.)
            Example: format_image=jpg

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

    @keyword
    def compare_image(
        self,
        base_image_path,
        compared_image_path,
        save_folder=default_output_folder,
        ssim=default_ssim,
        image_format=default_format_image,
    ) -> None:
        """
        Compares two images from and, if there are differences, saves the image with the errors highlighted into folder.

        Keyword Arguments:

            base_image_path {str} -- path to the first image to be compared

            compared_image_path {str} -- path to the second image to be compared

            save_folder {str} -- path to the folder where the image with differences will be saved

            ssim {float} -- threshold value in the interval (0, 1>. Tests pass, if ssim value returned by keyword is bigger than ssimm

            image_format {str} -- format for saving picture/screenshot (png, jpg etc.)

        Example
        | Compare image | login_baseline.png | login_new.png |
        """
        self.create_compare_images(
            base_image_path,
            compared_image_path,
            save_folder=save_folder,
            ssim=ssim,
            image_format=image_format,
        )

    @keyword
    def compare_image_without_areas(
        self,
        base_image_path,
        compared_image_path,
        *args,
        save_folder=default_output_folder,
        ssim=default_ssim,
        image_format=default_format_image,
    ) -> None:
        """
        Compares two pictures, which have areas to be ignored

        Keyword Arguments:
            
            x1 and y1 = x and y coordinates for the upper left corner of the ignored area square
        
            x2 and y2 = x and y coordinates for the lower right corner of the square of the ignored part

            Attention! Order of coordinates is as follows: x1 y1 x2 y2 x1 y1 x2 y2 etc ...

        Example: Creates 2 ignored areas at 0, 0, 30, 40 and 50, 50, 100, 100
        | Compare Image Without Areas | login.png | 0 | 0 | 30 | 40 | 50 | 50 |100 | 100 |
        """
        self.create_compare_image_without_areas(
            base_image_path,
            compared_image_path,
            *args,
            save_folder=save_folder,
            ssim=ssim,
            image_format=image_format,
        )

    @keyword
    def crop_image(
        self,
        path,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        save_folder=default_output_folder,
        image_format=default_format_image,
    ) -> None:
        """
        Comps picture

        x1 and y1 = x and y coordinates for the upper left corner of the cropping area
        
        x2 and y2 = x and y coordinates for the lower right corner of the cropping area

        Example: Crops image at coordinates 0, 0, 30, 40
        | Compare Image Without Areas | login.png | 0 | 0 | 30 | 40 |

        """
        self.create_crop_image(
            path=path,
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            save_folder=save_folder,
            image_format=image_format,
        )

    @keyword
    def rotate_image(
        self,
        path,
        screen_name="img",
        save_folder=default_output_folder,
        angle=0,
        image_format=default_format_image,
    ) -> None:
        """
        Rotates image by angle

        Keyword Arguments:

            path {str} - path to the picture we want to rotate.

            screen_name {str} - name of the screen, where the image is located.

            save_folder {str} - path to the folder where the rotated image will be saved.

            angle {Literal[0, 1, 2]} - rotation anlge: 0 = 90 degrees clockwise, 1 = 90 degrees counter clockwise, 2 = 180 degrees
        """
        self.create_rotate_image(
            path=path,
            screen_name=screen_name,
            save_folder=save_folder,
            angle=angle,
            image_format=image_format,
        )

    @keyword
    def pdf_to_image(
        self,
        path,
        save_folder=default_output_folder,
        screen_name="pdf_screen",
        page_number="-1",
        zoom="2",
    ) -> None:
        """
        Converts PDF to Image.

        Keyword Arguments:

            path {str} -- path to the PDF file to be converted.

            save_folder {str} -- path to the folder where the image will be saved.

            screen_name {str} -- name of the screen, where the image is located.

            page_number {str} -- page number of the PDF file to be converted.

            zoom {str} -- zoom level of the image.
        """
        self.convert_pdf_to_image(
            path=path,
            save_folder=save_folder,
            name=screen_name,
            page_number=page_number,
            zoom=zoom,
        )

    @keyword
    def return_text_from_area(
        self, path, page_number: int, x1: int, y1: int, x2: int, y2: int
    ) -> str:
        """
        Return text from area (without using tesseract).

        Keyword Arguments:

            path {str} -- path to the PDF file to be processed.

            page_number {int} -- page number of the PDF file to be processed.

            x1 {int} -- x coordinate of the upper left corner of the area.

            y1 {int} -- y coordinate of the upper left corner of the area.

            x2 {int} -- x coordinate of the lower right corner of the area.

            y2 {int} -- y coordinate of the lower right corner of the area.
        """
        return self.create_return_text_from_area(
            path=path, page_number=page_number, x1=x1, y1=y1, x2=x2, y2=y2
        )

    @keyword
    def should_exist_this_text(self, path, page_number: int, text: str) -> bool:
        """
        Checks if text exists in PDF on specified page and return TRUE if exists.

        Keyword Arguments:

            path {str} -- path to the PDF file to be processed.

            page_number {int} -- page number of the PDF file to be processed.

            text {str} -- text to be checked.
        """
        return self.create_should_exist_this_text(
            path=path, page_number=page_number, text=text
        )

    @keyword
    def image_to_string(
        self,
        path,
        oem="3",
        psm="3",
        language="eng",
    ) -> Union[bytes, str]:
        """
        Read text from image. 
        `*Note:* tesseract-ocr need to be installed.`

        Keyword Arguments:

            path {str} -- path to the image file to be processed.

            oem {str} -- Engine Mode (Settings from tesseract).

            psm {str} -- Page Segmentation Mode (Settings from tesseract).

            language {str} -- The language of the expected text to be read from picture, e.g. ces for Czech.
        """
        return self.create_image_to_string(
            path=path,
            oem=oem,
            psm=psm,
            language=language,
            path_to_tesseract=self.tesseract_path,
        )

    @keyword
    def image_area_on_text(
        self,
        path,
        *coordinates,
        oem="3",
        psm="3",
        language="eng",
    ) -> Union[list[str], str]:
        """
        Reading text from image.
        `*Note:* tesseract-ocr need to be installed.`
        
        Keyword Arguments:

            path {str} -- path to the image file to be processed.

            *coordinates -- coordinates where text is located. Must be 4 (x1, y1, x2, y2)

            oem {str} -- Engine Mode (Settings from tesseract).

            psm {str} -- Page Segmentation Mode (Settings from tesseract).

            language {str} -- The language of the expected text to be read from picture, e.g. ces for Czech.
        """
        return self.create_image_area_on_text(
            path,
            *coordinates,
            oem=oem,
            psm=psm,
            language=language,
            path_to_tesseract=self.tesseract_path,
        )
