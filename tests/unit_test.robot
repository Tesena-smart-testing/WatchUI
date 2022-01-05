*** Settings ***
Library                         SeleniumLibrary
Library                         Screenshot
Library                         OperatingSystem
Library                         ../WatchUI/WatchUI.py
Library                         OperatingSystem
Resource                        keywords/CS.robot
Resource                        keywords/CS_2SavedImage.robot
Resource                        keywords/CS_CreateScreens.robot
Resource                        keywords/CS_region.robot
Resource                        keywords/CS_CreateArea.robot
Resource                        keywords/Text_testing.robot
Resource                        keywords/Variable.robot
Test Setup                      Start web-browser
Test Teardown                   Close web-browser


*** Test Cases ***
TC01 - Compare two saved images
    [Tags]  tc01  compare_save_screen  VT
    [Setup]
    Compare 2 same images
    Compare images SSIM 0.5
    Compare images SSIM 0.5: JPG Format
    [Teardown]

TC02 - Creating screens in different resolutions
    [Tags]  tc02  resolution  VT
    Create screens in 800 x 600 reso
    Create screens in 3 resolutions
    Create screens with full set up
    Create screens with full set up: Format JPG

TC03 - Compare screen
    [Tags]  tc03  compare_screen  VT
    Compare image with created screen
    Compare image without full set up
    Compare image full set up
    Compare image without ssim set up
    Compare diff image ssim 0.5
    Compare diff image ssim 1.0
    Compare diff image image format JPG

TC04 - Compare screen without some region
    [Tags]  tc04  cs_outregion  VT  demo
    Comparing screen without some area: PNG Format

TC05 - Create Area
    [Tags]  tc05  create_area  VT
    Create area 200 x 500: basic
    Create area 200 x 500: full set up

TC06 - PDF and Tesseract
    [Tags]  tc06  TT  demo
    [Setup]
    Create IMG
    Create and compare vysvetlivky
    Check words                     ${CONTROLL_TEXT}     @{TEXT_COO}
    Read text from image
    Find diff in PDF
    [Teardown]

TC07 - Check text existence in PDF
    [Tags]  tc07  should_exist_this_text
    [Setup]
    ${Text_from_pdf}    Should exist this text  ${TT_path_to_pdf}   0   Dummy
    Should be true      ${Text_from_pdf} == True
    [Teardown]
    
TC08 - Check text existence in PDF
    [Tags]  tc08  return_text_from_area
    [Setup]
    ${Text_from_pdf}    Return text from area   ${TT_path_to_pdf}   0   50  60  190  90
    Should be true      '''${Text_from_pdf}''' == '''${TT_Should_be_text}'''
    [Teardown]

TC09 - Convert PDF to IMG
    [Tags]  tc09  pdf_to_img
    [Setup]
    Pdf to image            ${OK_PDF}               name=${NAME_OK_PDF}
    [Teardown]


*** Keywords ***
Start web-browser
    Open Browser                ${URL}      ${BROWSER}

Close web-browser
    Close Browser
