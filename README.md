# WatchUI
### Basic Info
Custom library for comparing images with use in Robot Framework. 
### What is here?
- Test robot/test.robot - file with examples how to use keywords
- WatchUI/WatchUI.py - file with keywords

# What you need
## Pip install

[WatchUI](https://pypi.org/project/WatchUI/)
1. Open CMD
2. Start `pip install WatchUI`
3. Now you can download WatchUI.py from repository or import WatchUI to new python file more [here](https://stackoverflow.com/questions/32952106/creating-a-robot-framework-library-from-existing-python-package)
4. If you download WatchUI.py: You must first enter the path in Settings => `Library          path`, where path is the path to the WatchUI.py file

## Manual Install
### Main
- [Python](https://www.python.org/)
- [RobotFramework](https://robotframework.org/)
- [OpenCV](https://opencv.org/)  `pip install opencv-python` or `pip3 install opencv-python`
- [Pillow](https://python-pillow.org/)    `pip install Pillow`
- [Numpy](https://numpy.org/) `pip install numpy`
- [Scikit](https://scikit-image.org/) `pip install scikit-image`
- [Imutils](https://github.com/jrosebr1/imutils) `pip install imutils`

### How to install in RF
- Download git file (Mainly ./Python/WatchUI.py)
- Enter the path in Settings => `Library          path`, where path is the path to the WatchUI.py file
- Now you can start using keywords listed below. Keep in mind that you need to have all dependencies installed.

## Description Keyword
### Images must have same resolution!!!!

- In folder Robot framework you can find some example
- You can settings two main value in import (`Library <path to WathUI>`)
- Applies to all TCs where it is not set directly at the key that the argument takes a different value

| Arguments | Documentation |
|    :---:      |     :---:      |
| outputs_folder= | The path where you want to save the image with the highlighted differences. Default folder is ../Outputs. Adjusting the Keywords has more weight than adjusting in import  |
| ssim_basic= | The lowest limit of difference between images when an RF gives you a pass. Takes values from 1.0E-12 to 1.0. Default ssim is 1.0 (100%) |

Example: `Library  WatchUI.py outputs_folder=../Myfolder ssim_basic=0.865`

| Keyword  | Arguments | Documentation |
|     :---:      |    :---:      |     :---      |
| Compare images  | path1, <br>path2, <br>save_folder=, <br>ssim=  |  This compares two images.  If there are differences it saves an image with the differences highlighted into the folder.</p>path1 = path to the first image to be compared<p>path2 =  path to the second image to be compared  <br>save_folder= the path where you want to save the image with the highlighted differences. Default folder is ../Outputs<br> ssim= The lowest limit of difference between images when an RF gives you a pass. Takes values from 1.0E-12 to 1.0. Default ssim is 1.0 (100%)   <p>Example:  `Compare two images  ../image1.png  ../Image2.png`  |
| Compare screen  | path1, <br>save_folder=, <br>ssim= |Compares a saved image with what is displayed on the screen. If there is a difference it saves an image with the differences highlighted to the save_folder </p>path1  = path to the image to be compared to screen<br>save_folder= the path where you want to save the image with the highlighted differences. Default folder is ../Outputs <br> ssim= The lowest limit of difference between images when an RF gives you a pass. Takes values from 1.0E-12 to 1.0. Default ssim is 1.0 (100%)  </p> Example:  `Compare screen  ../image1.png`  |
| Create area  | x1, y1, x2, y2,<br> screen_name=,  <br>save_folder=  | Creates a cut-out area of what is displayed on the screen and saves it in the folder: ../Create area  </p>x1 a y1 = x and y coordinates for the upper left corner of the square <p>x2 and y2 = x and y coordinates for the bottom right corner of the square<br>screen_name= the path where you want to save the image with the highlighted differences. Default name is (it is not mandatory to set it up)<br>save_folder= the path where you want to save the image with the cut out area. Default folder is ../Outputs <p> Example:  `Create area  0   0   25  25`  |
| Compare screen areas  | x1, y1, x2, y2, <br>path1, <br>save_folder=, <br>ssim=  | Compares area of the screen with a previously created cut out image area. </p>x1 and y1 = x and y coordinates for the upper left corner of the region <p>x2 and y2 = x and y coordinates for the bottom right corner of the region <br>path1 =   the path to an already created image (region) with which we want to compare the region selected at screen <br>save_folder= path where you want to save the image with the highlighted differences. Default folder is ../Outputs <br> ssim= The lowest limit of difference between images when an RF gives you a pass. Takes values from 1.0E-12 to 1.0. Default ssim is 1.0 (100%)</p>Example:  `Compare screen areas  0   0   25  25  ../Crop_Image1.png` |
| Compare screen without areas  | path1 <br>*args, <br>save_folder=, <br>ssim=  | Compares pictures (screenshot and image file) with areas to be ignored </p>x1 and y1 = x and y coordinates for the upper left corner of the area to be ignored  <p>x2 and y2 = coordinates for the lower right corner of the area to be ignored <br>save_folder= the path where you want to save the image with the highlighted differences. Default folder is ../Outputs <br> ssim= The lowest limit of difference between images when an RF gives you a pass. Takes values from 1.0E-12 to 1.0. Default ssim is 1.0 (100%)  <p>Attention! It is always necessary to enter in order x1 y1 x2 y2 x1 y1 x2 y2 etc ...  </p>Example: `Compare screen without areas ../Image1.png 0 0 30 40 50 50 100 100` <br> Creates 2 ignored parts at 0,0, 30,40 and 50, 50, 100, 100 |
| Create screens  | *resolution<br>save_folder=<br> screen_name=   | Creates a screenshot of the screen with specified resolution. It is possible in one command to create an infinite number of screens with different resolutions. Screens are stored in the folder: ../Create_screens </p>*resolution = The specified resolution in width and height format, you can enter as many as needed<br> save_folder= path where you want to save the image with the highlighted differences. Default folder is ../Create_screens <br>screen_name= the path where you want to save the image with the highlighted differences. Default name is (it is not mandatory to set it up) </p>Example: `compare making rescreens            800  600    1280    800     1440    900` <br>Creates 3 screens in 800x600 1280x800 and 1440x900 |
| Compare screen get information  | path1, <br>save_folder=, <br>folder_csv=, <br>ssim=  |Compares an already saved image with what is displayed on the screen. If there is a difference, it saves an image with the highlighted differences to the: ../save_folder and creates a csv file with the coordinates and elements that exist on those coordinates <p> *path1 = path to the image to be compared</p> *path1 = path to the image to be compared <br>save_folder= path where you have save img Default folder is ../Outputs<br> folder_csv= folder for csv file with save coordinates. Default folder is ../CSV_ERROR <br> ssim= The lowest limit of difference between images when an RF gives you a pass. Takes values from 1.0E-12 to 1.0. Default ssim is 1.0 (100%)</p>Example:     `compare screen get information      1c.png`<br> Compare img 1c.png with screen and save img with diff and save csv file with elements on this coordinates |

## Sample results

_Image where the differences are stored + You can see two black box in left corner. These black box are ignored during comparison._

<img src="/Img/logscreen.png" width="850" height="300">

_The red rectangles outlining missing elements on compared screens_

<img src="/Img/img_inlog.png" width="850" height="300">

