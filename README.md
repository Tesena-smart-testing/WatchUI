# WatchUI

### Basic Info

Custom library for comparing images with use in Robot Framework.

### What is here?

- Test samples/test.robot - file with examples how to use keywords
- WatchUI/WatchUI.py - file with keywords

# What you need

## Pip install

[WatchUI](https://pypi.org/project/WatchUI/)

1. Open CMD
2. Start `pip install WatchUI`
3. Now you can download WatchUI.py from repository or import WatchUI to new python file more [here](https://stackoverflow.com/questions/32952106/creating-a-robot-framework-library-from-existing-python-package)
4. If you download WatchUI.py: You must first enter the path in Settings => `Library path`, where path is the path to the WatchUI.py file

## Manual Install

### Main

- [Python](https://www.python.org/)
- [RobotFramework](https://robotframework.org/)
- [OpenCV](https://opencv.org/) `pip install opencv-python` or `pip3 install opencv-python`
- [Pillow](https://python-pillow.org/) `pip install Pillow`
- [Numpy](https://numpy.org/) `pip install numpy`
- [Scikit](https://scikit-image.org/) `pip install scikit-image`
- [Imutils](https://github.com/jrosebr1/imutils) `pip install imutils`

### How to install in RF

- Download git file (Mainly ./Python/WatchUI.py)
- Enter the path in Settings => `Library path`, where path is the path to the WatchUI.py file
- Now you can start using keywords listed below. Keep in mind that you need to have all dependencies installed.

## Description Keyword

Library documentation can be found [HERE](https://tesena-smart-testing.github.io/WatchUI/).

## Sample results

_Image where the differences are stored + You can see two black box in left corner. These black box are ignored during comparison._

<img src="/Img/logscreen.png" width="850" height="300">

_The red rectangles outlining missing elements on compared screens_

<img src="/Img/img_inlog.png" width="850" height="300">
