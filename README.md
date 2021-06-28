# WatchUI

## [Documentation](https://tesena-smart-testing.github.io/WatchUI/) | [Tesena](https://www.tesena.com/) | [Pypi](https://pypi.org/project/WatchUI/)

### Basic Info

Robot Framework visual testing library for visual difference testing as well as image content testing (including PDF documents).
Runs on Selenium or Playwright to generate screenshots, PyMuPDF to process PDFs and Tesseract OCR to recognize text.

### Project structure

```
WatchUI
└── .github/workflows           # All github actions definitions for CI
└── Img                         # Test and demo data
└── WatchUI                     # WatchUI library implementation
│    └── WatchUI.py             # Implementation file
└── tests                       # Tests and examples in Robot Framework
│    └── keywords               # More tests for keywords and definitions of variables
│    └── unit_test.robot        # Basic unit tests
└── README.MD                   # Here you are :-)
└── setup.py                    # File for easy setup use with pip install .
```

### Install

For quick start use:

```
pip install WatchUI
```

For more details see our [Documentation](https://tesena-smart-testing.github.io/WatchUI/).

### Sample results

_Comparison of two screens where the differences are showed by red rectangles. In this example we ignored the dynamic boxes during comparison. These boxes were overlaid by black rectangles (the right on the pictures) ._

<img src="https://raw.githubusercontent.com/Tesena-smart-testing/WatchUI/master/Img/logscreen.png" width="850" height="300">

_The red rectangles outlining missing elements on compared screens. In this case pictures are completely different due to bot protection feature during retesting._

<img src="https://raw.githubusercontent.com/Tesena-smart-testing/WatchUI/master/Img/img_inlog.png" width="850" height="300">

### Development

1. Clone this repository
2. Create `.venv` `python -m venv .venv`
3. Activate `.venv`
   - [VS Code](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment): _Ctrl+Shift+P_, select option _Python: Select Interpreter_
   - [PyCharm](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#interpreter): _Ctrl+Alt+S_, select _Project <project name>_ | _Python Interpreter_.
4. Install all required packages `pip install -r requirements.txt`
5. Download [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/home)
6. Install [tesseract] (https://tesena-smart-testing.github.io/WatchUI/start.html#install-tesseract)
   _Note: In order to get test case within `unit_test.robot` working you have install also Czech language_
7. Run tests `python -m robot tests/unit_test.robot` or just `robot tests/unit_test.robot`

_Note: If tesseract is not installed you can still use many features of WatchUI. Currently WatchUI need tesseract only if you need to use keywords: `Image to string`, `Image area on text` and `Return text from area`_
