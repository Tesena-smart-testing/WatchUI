test case

yes

WatchUI - Custom library for comparing images with use in Robot
Framework. = Table of Contents = - \`Usage\` - \`Importing\` -
\`Examples\` - \`Keywords\` = Usage = This library allows for automated
visual testing of web frontends. Currently, this library is not
officialy supported, so best way is to clone the repository and copy the
WatchUI.py library file into your project and then import it - see
Importing section. However, you can also install it via command \*pip
install WatchUI\* and then import it. \*IMPORTANT\*: When using keywords
of this library, please remember, that screenshots have to have same
resolution! = Examples = Import library \| \`Library\` \|
\<path_to_library file\> \| outputs_folder= \| ssim_basic= \|
starts_format_image= \| Compare Images \| Compare Images \| path1 \|
path2 \| save_folder= \| ssim= \| starts_format_image= \|

outputs_folder=../Outputs

ssim_basic=1.0

format_image=png

Library can be imported either with default output folder and set lowest
limit of difference between images (ssim), or you can provide your own
values. Keyword Arguments: outputs_folder {str} \-- path, where you want
to save images with highlighted differences (default: \"../Outputs\")
ssim_basic {float} \-- threshold value in the interval (0, 1\>. Tests
are passed, if ssim value returned by keyword test functions is bigger
than this (default: 1.0) format_image {str} \-- Format for saving
picture/screenshot (png, jpg etc.) Example: format_image=jpg (default:
png) Examples: \| =Setting= \| =Value= \| =Value= \| =Value= \|
=Comment= \| \| Library \| WatchUI.py \| \| \| \# Uses default values of
keyword arguments \| \| Library \| WatchUI.py \|
outputs_folder=\<path_to_folder\> \| \| \# changes folder to different
one \| \| Library \| WatchUI.py \| outputs_folder=\<path_to_folder\> \|
ssim_basic=\<float\> \| \# changes output folder and ssim threshold \|

path1

path2

save_folder=../Outputs

ssim=1.0

image_format=png

Comparing images It compares two images from the two paths and, if there
are differences, saves the image with the errors highlighted in the
folder: ../Save Image path1 = path to the first image to be compared
path2 = path to the second image to be compared Example: Compare two
image ../image1.png ../Image2.png

path1

save_folder=../Outputs

ssim=1.0

image_format=png

Compare the already save image with the browser screen Compares the
already saved image with the screen that is on the screen. If there is a
difference, it saves the highlighted image to the: ../Save Image path1 =
path to the image to be compared to screen Example: Compare screen
../image1.png

x1

y1

x2

y2

path1

save_folder=../Outputs

ssim=1.0

image_format=png

Creates a cut-out from the screen Creates a cut-out from the screen that
is on the screen and compares it to a previously created x1 and y1 = x
and y coordinates for the upper left corner of the square x2 and y2 = x
and y coordinates for the bottom right corner of the square path1 = Path
to an already created viewport with which we want to compare the
viewport created by us Example: Compare screen area 0 0 25 25
../Crop_Image1.png Creates Crop_Image1.png from 0, 0, 25, 25

path1

save_folder=../Outputs

folder_csv=../CSV_ERROR

ssim=1.0

image_format=png

Compare the already save image with the browser screen Compares the
already saved image with the screen that is on the screen. If there is a
difference, it saves the highlighted image to the: ../Save Image and
making csv file with coordinates and elements which exist on this
coordinates path1 = path to the image to be compared to screen Example:
Compare screen ../image1.png

path1

\*args

save_folder=../Outputs

ssim=1.0

image_format=png

Compares two pictures, which have parts to be ignored x1 and y1 = x and
y coordinates for the upper left corner of the ignored area square x2
and y2 = x and y coordinates for the lower right corner of the square of
the ignored part Attention! It is always necessary to enter in order x1
y1 x2 y2 x1 y1 x2 y2 etc \... Compare screen without areas ../Image1.png
0 0 30 40 50 50 100 100 Creates 2 ignored parts at 0,0, 30,40 and 50,
50, 100, 100

x1

y1

x2

y2

save_folder=../Outputs

screen_name=screen

image_format=png

Creates a cut-out from the screen Creates a cut-out from the screen that
is on screen and saves it in the folder: ../Create area x1 a y1 = x and
y coordinates for the upper left corner of the square x2 and y2 = x and
y coordinates for the bottom right corner of the square Example: Compare
making area 0 0 25 25

\*resolution

save_folder=../Outputs

screen_name=screen

image_format=png

Creates a screenshot on the screen Creates a screenshot on the screen,
that corresponds to the specified resolution, so it is possible to
create on one page an infinite number of screens with different
resolutions. Screens are stored in the folder: ../Create rescreens
\*resolutin = The specified resolution in width and height format, you
can enter as many as needed Warning: When you create one screen, name
will be screen.png, but when you create more than one screen from same 4
page, name will be screen screen_name_width_height.png Example: compare
making rescreens 800 600 1280 800 1440 900 Creates 3 screens in 800x600
1280x800 and 1440x90
