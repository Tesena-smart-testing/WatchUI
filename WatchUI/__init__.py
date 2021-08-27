import os
from WatchUI.keywords import *
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError


class WatchUI(_VisualKeywords):
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
        | `Library` | <path_to_library file> | outputs_folder= | ssim_basic= |

        Compare Images
        | Compare Images | path1 | path2 | save_folder= | ssim= |

        """

    save_folder_path = "../Outputs"
    starts_ssim = 1.0
    starts_format_image = "png"

    def __init__(self, outputs_folder=save_folder_path, ssim_basic=starts_ssim, format_image=starts_format_image):
        """Library can be imported either with default output folder and set lowest limit of difference between images (ssim), or
        you can provide your own values.

        Keyword Arguments:

            outputs_folder {str} -- path, where you want to save images with highlighted differences (default: "../Outputs")

            ssim_basic {float} -- threshold value in the interval (0, 1>. Tests are passed, if ssim value returned by keyword test functions is bigger than this (default: 1.0)

            format_image {str} -- Format for saving picture/screenshot (png, jpg etc.) Example: format_image=jpg (default: png)

        Examples:

        | =Setting= | =Value= | =Value= | =Value= | =Comment= |
        | Library   | WatchUI.py |      |  | # Uses default values of keyword arguments |
        | Library   | WatchUI.py | outputs_folder=<path_to_folder> | | # changes folder to different one |
        | Library   | WatchUI.py | outputs_folder=<path_to_folder> | ssim_basic=<float> | # changes output folder and ssim threshold |

        """
        self.outputs_folder = outputs_folder
        self.ssim_basic = float(ssim_basic)
        self.image_format = str(format_image)
        # when libdoc builds documentation, this would lead to exception, since robot cannot access execution context,
        # since nothing really executes
        try:
            self.seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
            self.robotlib = BuiltIn().get_library_instance("BuiltIn")
        except RobotNotRunningError as e:
            print(
                f"If you are trying to build documentation, than this exception is just nuisance, skipping...\n{str(e)}"
            )
            pass
        self.score = None
        self.cnts = None
        self.img1 = None
        self.img2 = None