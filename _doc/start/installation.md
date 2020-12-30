---
title: Installation
sections:
  - Install WatchUI
  - Install Tesseract
---

### Install WatchUI

#### Pip install

For Installing WatchUI you need [python >= 3.5](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installing/)

Installation with pip:

```shell
pip install WatchUI
```

In order to use library in Robot Framework just simply import library within Setting sections:

```robotframework
*** Settings ***
Library         WatchUI
```

#### From github (alternative)

Alternatively WatchUI can be installed by grabbing the library directly from GitHub repository.
For that it is required to have installed:

- [python >= 3.5](https://www.python.org/),
- [pip](https://pip.pypa.io/en/stable/installing/) and
- [git](https://git-scm.com/)

If you have git, go to project folder and use in cmd:

```shell
git pull https://github.com/Tesena-smart-testing/WatchUI.git
```

Library needs to install some dependencies before we can use it. All required libraries can be found in the requirements.txt file within [WatchUI repository](https://github.com/Tesena-smart-testing/WatchUI) and simply installed by pip:

```shell
pip install -r requirements.txt
```

To use it in Robot framework it need to be imported by providing full path to implementation file:

```robotframework
*** Settings ***
Library  <path to folder where is WatchUI.py>/WatchUI.py
```

### Install Tesseract

Tesseract OCR need to be installed additionally to the standard installation mentioned above and it will be needed only if you need to use the keyword using the library: [keywords using Tesseract OCR](https://tesena-smart-testing.github.io/WatchUI/keywords.html#keyword-breakdown).

#### Windows

{: .list}

- Download the latest released version of the Windows installer for Tesseract [from here](https://digi.bib.uni-mannheim.de/tesseract/)
- Run the executable file to install. It will be installed to C:\Program Files (x86)\Tesseract OCR
- Make sure your TESSDATA_PREFIX environment variable is set correctly:
  - Go to Control Panel -> System -> Advanced System Settings -> Advanced tab -> Environment Variables... button
  - In System variables window scroll down to TESSDATA_PREFIX. If it's not right, select and click Edit

#### Debian / Ubuntu

```shell
apt-get install tesseract-ocr
```

By default Tesseract will install the English language pack, to install additional languages run:

```shell
apt-get install tesseract-ocr-LANG
```

where LANG is language.
