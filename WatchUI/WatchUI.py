# pylint: disable=invalid-name, line-too-long, too-many-arguments
"""
Library module
"""

from .keywords import Image, Pdf, Tesseract


class WatchUI(Image, Pdf, Tesseract):
    """WatchUI - Custom library for comparing images with use in Robot Framework.
    = Table of Contents =
    - `Usage`
    - `Importing`
    - `Examples`
    - `Keywords`
    = Usage =
    This library allows for automated visual testing of web frontends.
    *IMPORTANT*: When using keywords of this library, please remember,
    that screenshots have to have same resolution!
    = Examples =
    Import library
    | `Library` | <path_to_library file> | outputs_folder= | ssim_basic= | format_image= | tesseract_path=
    Compare Images
    | Compare Images | path1 | path2 | save_folder= | ssim= | format_image= |
    """

    def __init__(
        self,
        outputs_folder="./outputs",
        ssim_basic=1.0,
        format_image="png",
        tesseract_path=r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    ):
        """Library can be imported either with default output folder and set
        lowest limit of difference between images (ssim), or
        you can provide your own values.
        Keyword Arguments:
            outputs_folder {str} -- path, where you want to save images with highlighted
            differences (default: "../Outputs")
            ssim_basic {float} -- threshold value in the interval (0, 1>. Tests are passed,
            if ssim value returned by keyword test functions is bigger than this (default: 1.0)
            format_image {str} -- Format for saving picture/screenshot (png, jpg etc.)
            tesseract_path {str} -- path for tesseract
            Example: format_image=jpg (default: png)
        Examples:
        | =Setting= | =Value= | =Value= | =Value= | =Comment= |
        | Library   | WatchUI |      |  | # Uses default values of keyword arguments |
        | Library   | WatchUI | outputs_folder=<path_to_folder> | | # changes folder to different one |
        | Library   | WatchUI | outputs_folder=<path_to_folder> | ssim_basic=<float> | # changes output folder and ssim threshold |
        """
        super().__init__(outputs_folder, ssim_basic, format_image, tesseract_path)
