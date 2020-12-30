---
title: Basic Guide
sections:
  - Basic usage WatchUI in test
  - Basic usage Tesseract and WatchUI in test
---

### Basic usage WatchUI in test

After installation we create new file test.robot with:

```robotframework
*** Settings ***

*** Variables ***

*** Test Cases ***

*** Keywords ***

```

Within `Settings` section import Selenium and WatchUI libraries.

```robotframework
*** Settings ***
Library         SeleniumLibrary
Library         Screenshot
Library         WatchUI.py
```

Create a set of variables (browser and url) we later use for Selenium, e.g. browser = Chrome and Url = tesla.com:

```robotframework
*** Variables ***
${start_url}        https://www.tesla.com/
${browser}          Chrome
```

In order to compare actual page opened by Selenium (screenshot) with image saved in folder (path to image need to be included) we use keyword `Compare screen`:

```robotframework
*** Keywords ***
Compare screen with image
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    Sleep                               7
    Compare screen                      ./Outputs/screen800x600.png
```

Now we just create Test case:

```robotframework
*** Test Cases ***
Sample test
    Compare screen with image
```

Ours final file looks like:

```robotframework
*** Settings ***
Library         SeleniumLibrary
Library         Screenshot
Library         WatchUI

*** Variables ***
${start_url}        https://www.tesla.com/
${browser}          Chrome

*** Test Cases ***
Sample test
    Compare screen with image

*** Keywords ***
Compare screen with image
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    Sleep                               7
    Compare screen                      ./Outputs/screen800x600.png
```

Now just starts robot and thats it.

### Basic usage Tesseract OCR and WatchUI in test

This approach is recommended when we need to test content of PDF files and standard strategy of text recognition (using PyMuPDF keywords) doesn't work. Same applies for testing content of images.

For this cases we implemented two keywords using Tesseract OCR:

```robotframework
Image to string
```

and:

```robotframework
Image area on text
```

In this example we have a pdf and we want to extract the text from area at coordinates 0, 0, 179, 83.

We start with settings:

```robotframework
*** Settings ***
Library         WatchUI
```

After settings we must set up ours variables as

<div class="table-responsive">

{: .table}
| Variables | Description
|-
| ${TT_path_to_pdf} | Path to the tested PDF file
| ${TT_name_img} | Name of the new image, which we create from PDF
| ${TT_path_to_img} | Path to the new image ${TT_name_img}
| @{TT_text_area_coo} | Area coordinates, where from we want to read text
| ${TT_should_be_text} | Text we are expecting

</div>

```robotframework
*** Variables ***
${TT_path_to_pdf}          ../Img/dummy.pdf
${TT_name_img}              pdfInPng
${TT_path_to_img}          ../Outputs/${TT_name_img}.png
@{TT_text_area_coo}        0    0   179     83
${TT_should_be_text}        Dummy PDF file
```

Now we can finally create keywords:

1. From pdf to image
2. Extract data from image to variables and then compare values.

```robotframework
*** Keywords ***
Convert PDF to IMG
    pdf to image    ${TT_path_to_pdf}   name=${TT_name_img}  save_folder=../Outputs/

From IMG to string
    ${Text_from_area}   Image area on text   ${TT_path_to_img}  @{TT_text_area_coo}     psm=10
    Should Be True                          '''${Text_from_area}''' == '''${TT_should_be_text}'''
```

Final code is:

```robotframework
*** Settings ***
Library         WatchUI


*** Variables ***
${TT_path_to_pdf}          ../Img/dummy.pdf
${TT_name_img}             pdfInPng
${TT_path_to_img}          ../Outputs/${TT_name_img}.png
@{TT_text_area_coo}        0    0   179     83
${TT_should_be_text}       Dummy PDF file


*** Test Cases ***
Sample test
    Convert PDF to IMG
    From IMG to string


*** Keywords ***
Convert PDF to IMG
    pdf to image    ${TT_path_to_pdf}   name=${TT_name_img}  save_folder=../Outputs/

From IMG to string
    ${Text_from_area}   Image area on text   ${TT_path_to_img}  @{TT_text_area_coo}     psm=10
    Should Be True                          '''${Text_from_area}''' == '''${TT_should_be_text}'''
```
