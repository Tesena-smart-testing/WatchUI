from setuptools import setup, find_packages
from sys import platform


try:
    if platform.startswith("linux"):
        setup(
            name="WatchUI",
            packages=find_packages(),
            install_requires=[
                "opencv-python",
                "Pillow",
                "numpy",
                "scikit-image",
                "imutils",
                "robotframework",
                "robotframework-seleniumLibrary",
            ],
        )
    else:
        raise OSError(
            "Setup.py runs correctly only in linux at this time. Sorry for that. \
            \nPlease install packages manually on other systems."
        )
except OSError as e:
    print(f"{e}")
