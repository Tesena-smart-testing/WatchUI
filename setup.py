from setuptools import setup, find_packages
from sys import platform

with open("README.md", "r") as f:
    long_description = f.read()

try:
    if platform.startswith("linux"):
        setup(
            name="WatchUI",
            author="Jan Egermaier, Radek Bednarik",
            author_email="jan.egermaier@tesena.com",
            description="RobotFramework library package for automated visual testing.",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/Tesena-smart-testing/WatchUI",
            packages=find_packages(),
            install_requires=[
                "opencv-python",
                "pandas",
                "Pillow",
                "numpy",
                "scikit-image",
                "scikit-learn",
                "imutils",
                "robotframework",
                "selenium",
                "robotframework-seleniumLibrary",
            ],
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
            python_requires=">=3.6",
        )
    else:
        raise OSError(
            "Setup.py runs correctly only in linux at this time. Sorry for that. \
            \nPlease install packages manually on other systems."
        )
except OSError as e:
    print(f"{e}")
