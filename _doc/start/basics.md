---
title: Basic Guide
sections:
  - Basic usage WatchUI in test
  - Basic usage Tesseract+WatchUI in test
---

### Basic usage WatchUI in test
After installation we create new file test.robot with:

```robotframework
*** Settings ***

*** Variables ***

*** Test Cases ***

*** Keywords ***

```

We need to import under settings Selenium and WatchUI. Set up Test teardown for close browser and dont forget on Documentation.
```robotframework
*** Settings ***
Documentation   Suite description
Library         SeleniumLibrary
Library         Screenshot
Library         WatchUI.py
Test Teardown   Close All Browsers
```

Now we create a simple variable for selenium. Because we wanna use Chrome as browser and Url will be tesla. We put to the code:
```robotframework
*** Variables ***
${start_url}        https://www.tesla.com/
${browser}          Chrome
```

After variables we want to compare screenshot which we have in folder with webpage. So we create keywords for comparing screenshot and webpage. 

In keyword compare screen we must set up path to image which we want to compare with screen
```robotframework
*** Keywords ***
Screen compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    Sleep                               7
    Compare screen                      ./Outputs/screen800x600.png
```

Now we just create Test case:
```robotframework
*** Test Cases ***
Sample test
    NOK Screen compare
```

Ours final file looks like:
```robotframework
*** Settings ***
Documentation   Suite description
Library         SeleniumLibrary
Library         Screenshot
Library         WatchUI.py
Test Teardown   Close All Browsers

*** Variables ***
${start_url}        https://www.tesla.com/
${browser}          Chrome

*** Test Cases ***
Sample test
    NOK Screen compare

*** Keywords ***
Screen compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    Sleep                               7
    Compare screen                      ./Outputs/screen800x600.png
```

Now just starts robot and thats all :-)

### Basic usage Tesseract + WatchUI in test
We need test pdf file and sometimes it happens that search in text doesnt work. We dont talk about why this happens sometimes (You can try google python pdf data mining). Or we need check that image which we create in system has right value.

For this problems I create two keywords:
```robotframework
Image to string
```

and:

```robotframework
Image area on text
```

In my case we have a pdf and we wanna extract the text at coordinates 0,0,179,83.

We start with settings:
```robotframework
*** Settings ***
Documentation   Suite description
Library         WatchUI.py
```

After settings we must set up ours variables as
<div class="table-responsive">

{: .table}
| Variables | Documentation
|-
| ${TT_path_to_pdf} | path to the pdf
| ${TT_name_img} | Name of the new image, which we create from pdf
| ${TT_path_to_img} | Path to the new image
| @{TT_text_area_coo} | Area coordinates, where we wanna read text
| ${TT_Should_be_text} | Text we are expect

</div>

```robotframework
*** Variables ***
${TT_path_to_pdf}          ../Img/dummy.pdf
${TT_name_img}              pdfInPng
${TT_path_to_img}          ../Outputs/${TT_name_img}.png
@{TT_text_area_coo}        0    0   179     83
${TT_Should_be_text}        Dummy PDF file
```

Now we can finally create keywords.
1. From pdf to image
2. Extract data from image to variables and then compare values.

```robotframework
*** Keywords ***
Convert PDF to IMG
    pdf to image    ${TT_path_to_pdf}   name=${TT_name_img}  save_folder=../Outputs/


From IMG to string
    ${Text_from_area}   Image area on text   ${TT_path_to_img}  @{TT_text_area_coo}     psm=10
     should be true                          '''${Text_from_area}''' == '''${TT_Should_be_text}'''
```

Final code is:

```robotframework
*** Settings ***
Documentation   Suite description
Library         WatchUI.py


*** Variables ***
${TT_path_to_pdf}          ../Img/dummy.pdf
${TT_name_img}              pdfInPng
${TT_path_to_img}          ../Outputs/${TT_name_img}.png
@{TT_text_area_coo}        0    0   179     83
${TT_Should_be_text}        Dummy PDF file

*** Test Cases ***
Sample test
    Convert PDF to IMG
    From IMG to string

*** Keywords ***
Convert PDF to IMG
    pdf to image    ${TT_path_to_pdf}   name=${TT_name_img}  save_folder=../Outputs/


From IMG to string
    ${Text_from_area}   Image area on text   ${TT_path_to_img}  @{TT_text_area_coo}     psm=10
     should be true                          '''${Text_from_area}''' == '''${TT_Should_be_text}'''
```