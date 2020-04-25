*** Settings ***
Documentation                   Suite description
Library                         SeleniumLibrary
Library                         Screenshot
Library                         ./WatchUI/WatchUI.py
Library                         OperatingSystem
Resource                        keywords/CS.robot
Resource                        keywords/CS_2SavedImage.robot
Resource                        keywords/CS_CreateScreens.robot
Resource                        keywords/CS_region.robot
Resource                        keywords/Variable.robot
Test Setup                      Start web-browser
Test Teardown                   Close web-browser

*** Test Cases ***
TC01 - Compare two saved images
    [Tags]  compare_save_screen     tc01
    [Setup]
    Compare 2 same images
    Compare images SSIM 0.5
    [Teardown]

TC02 - Creating screens in differen resolutions
    [Tags]  resolution  tc02
    Create screens in 800 x 600 reso
    Create screens in 3 resolutions
    Create screens with full set up

TC03 - Compare screen
    [Tags]  compare_screen  tc03
    Compare image with created screen
    Compare image full set up
    Compare diff image

TC04 - Compare screen without some region
    [Tags]  cs_outregion
    Comparing screen without some area

*** Keywords ***
Start web-browser
    Open Browser                ${URL}      ${BROWSER}
Close web-browser
    Close Browser
