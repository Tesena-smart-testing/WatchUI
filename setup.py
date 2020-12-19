from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="WatchUI",
    version="2.0.0",
    author="Jan Egermaier",
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
        "PyMuPDF",
        "pytesseract",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
