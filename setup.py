from setuptools import setup, find_packages
from sys import platform

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="WatchUI",
    version="1.0.11",
    author="Jan Egermaier",
    author_email="jan.egermaier@tesena.com",
    description="RobotFramework library package for automated visual testing.",
    long_description=open("README.md", encoding="utf-8").read(),
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
        "PyMuPDF",
        "pytesseract"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="<3.9",
)
