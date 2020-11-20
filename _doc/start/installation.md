---
title: Installation
sections:
  - Install WatchUI
  - Install Tesseract
---
### Install WatchUI

#### Pip install

For Installing WatchUI needs [python >= 3.5](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installing/)

If you have pip you can use just:

```shell
pip install WatchUI
```

and to the Robot framework put just:

```robotframework
*** Settings ***
Library         WatchUI
```

#### From github
For Installing WatchUI needs [python >= 3.5](https://www.python.org/), [pip](https://pip.pypa.io/en/stable/installing/) and [git](https://git-scm.com/)

If you have git, go to project folder and use in cmd:
```shell
git pull https://github.com/Tesena-smart-testing/WatchUI.git
```

Library needs some requirements, which you can find in file requirements.txt in [repository](https://github.com/Tesena-smart-testing/WatchUI)
```shell
pip install -r requirements.txt
```

and to the Robot framework put just:

```robotframework
*** Settings ***
Library  <path to folder where is WatchUI.py>/WatchUI.py
```


### Install Tesseract
#### Windows
{: .list}
- Download the latest released version of the Windows installer for Tesseract. Last version you can find [here](https://digi.bib.uni-mannheim.de/tesseract/)
- Run the executable file to install. It will install to C:\Program Files (x86)\Tesseract OCR
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