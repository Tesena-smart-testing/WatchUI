# WatchUI
### Basic Info
Custom library for comparing images with use in RobotFramework. It can be used as free functions to import into another language, but be careful because i used some command for robot framework (loggin etc.).In the future we will also create a library for python + selenium. <br>RF example: `Library          path` Python example:`import robotframework.py`

### What is here?
- Test robot/test.robot - file with example how to use keyword
- Watchmen/robotframework.py - file with keywords

# What you need
## Pip install

[WatchUI](https://pypi.org/project/WatchUI/)
1. Open CMD
2. Start `pip install WatchUI`
3. Import to robotframework `Library WatchUI` or `Library WatchUI/robotframework.py`

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
- Download git file (Mainly ./Python/robotframework.py)
- You must first enter the path in Settings => `Library          path`, where path is the path to the robotframework.py file
- Now, you can start using keywords listed below. Keep in mind that you need to have everything installed in order for it to work properly

## Description Keyword
### It is always necessary to ensure that the images are the same resolution (size) !!!!

- In folder Test robot you can find some example :-)

| Keyword  | Arguments | Documentation |
|     :---:      |    :---:      |     :---      |
| Compare two image  | path1, <br>path2, <br>save_folder=  |  This compares two images from two folders.  If there are differences it saves an image with the differences highlighted into the folder:  ../Compare two Images </p>path1 = path to the first image to be compared<p>path2 =  path to the second image to be compared  <br>save_folder= the path where you want to save the image with the highlighted differences. Basic settings is ../Compare two Images (it is not mandatory to set it up)  <p>Example:  Compare two image  ../image1.png  ../Image2.png  |
| Compare screen  | path1, <br>save_folder= |Compares a saved image with what is displayed on the screen. If there is a difference it saves an image with the differences highlighted to the: ../Save Image  </p>path1  = path to the image to be compared to screen<br>save_folder= the path where you want to save the image with the highlighted differences. Basic settings is ../Save Image (it is not mandatory to set it up)  </p> Example:  Compare screen  ../image1.png  |
| Compare making area  | x1, y1, x2, y2, <br>save_folder=  | Creates a cut-out area of what is displayed on the screen and saves it in the folder: ../Create area  </p>x1 a y1 = x and y coordinates for the upper left corner of the square <p>x2 and y2 = x and y coordinates for the bottom right corner of the square<br>save_folder= the path where you want to save the image with the cut out area. Basic settings is ../Create area (it is not mandatory to set it up)<p> Example:  Compare making area  0   0   25  25  |
| Compare screen area  | x1, y1, x2, y2, <br>path1, <br>save_folder=  | Compares and area of the screen with a previously created cut out image area x1 and y1 = x and y coordinates for the upper left corner of the screen area to compare </p>x1 and y1 = x and y coordinates for the upper left corner of the square <p>x2 and y2 = x and y coordinates for the bottom right corner of the square <br>path1 =   Path to an already created viewport with which we want to compare the viewport created by us <br>save_folder= path where you want to save the image with the highlighted differences. Basic settings is ../Save Image area (it is not mandatory to set it up)</p>Example:  Compare screen area  0   0   25  25  ../Crop_Image1.png `Creates Crop_Image1.png from 0, 0, 25, 25`|
| Compare screen without areas  | path1 <br>*args, <br>save_folder=  | Compares two pictures with areas to be ignored </p>x1 and y1 = x and y coordinates for the upper left corner of the area to be ignored  <p>x and y coordinates for the lower right corner of the area to be ignored <br>save_folder= the path where you want to save the image with the highlighted differences. Basic settings is ../Save Image areas<p>Attention! It is always necessary to enter in order x1 y1 x2 y2 x1 y1 x2 y2 etc ... </p>Compare screen without areas ../Image1.png 0 0 30 40 50 50 100 100 `Creates 2 ignored parts at 0,0, 30,40 and 50, 50, 100, 100` |
| Compare making rescreens  | *resolution  | Creates a screenshot of the screen with specified resolution. It is possible in one command to create an infinite number of screens with different resolutions. Screens are stored in the folder: ../Create rescreens </p>resolutin = The specified resolution in width and height format, you can enter as many as needed </p>Example: compare making rescreens            800  600    1280    800     1440    900 `Creates 3 screens in 800x600 1280x800 and 1440x900` |
| Compare screen get information  | path1, <br>save_folder=, <br>folder_csv=  |Compares an already saved image with what is displayed on the screen. If there is a difference, it saves an image with the highlighted differences to the: ../save_folder and creates a csv file with the coordinates and elements that exist on those coordinates <p> *path1 = path to the image to be compared</p> *path1 = path to the image to be compared <br>save_folder= path where you have save img<br> folder_csv= folder for csv file with save coordinates. Basic settings is ../CSV_ERROR (it is not mandatory to set it up</p>Example:     compare screen get information      1c.png `Compare img 1c.png with screen and save img with diff and save csv file with elements on this coordinates` |

## How it looks screen

_Image where the differences are stored + You can see two black box in left corner. These black box are ignored in compare._

<img src="/img/logscreen.png" width="850" height="300">

_Image can u see in the log, red rectangle are mising or not existing elements on web_

<img src="/img/img_inlog.png" width="850" height="300">



