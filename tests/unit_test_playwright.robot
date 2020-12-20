*** Settings ***
Documentation                   Suite description
Library                         Browser
Library                         Screenshot
Library                         OperatingSystem
Library                         WatchUI    playwright
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
    [Tags]  compare_save_screen     tc01    VT
    # for Playwright, you have to have browser instance running, otherwise
    # no screenshots via browser instance, sorry
    # [Setup]
    Compare 2 same images
    Compare images SSIM 0.5
    Compare images SSIM 0.5: JPG Format
    # [Teardown]

TC02 - Creating screens in differen resolutions
    [Tags]  resolution  tc02        VT
    Create screens in 800 x 600 reso
    Create screens in 3 resolutions
    Create screens with full set up
    Create screens with full set up: Format JPG

TC03 - Compare screen
    [Tags]  compare_screen  tc03    VT
    Compare image with created screen
    Compare image without full set up
    Compare image full set up
    Compare image without ssim set up
    Compare diff image ssim 0.5
    Compare diff image ssim 1.0
    Compare diff image image format JPG

TC04 - Compare screen without some region
    [Tags]  cs_outregion    VT
    Comparing screen without some area: PNG Format
    Comparing screen without some area: JPG Format

TC05 - Create Area
    [Tags]  create_area  tc05   VT
    Create area 200 x 500: basic
    Create area 200 x 500: full set up

TC06 - Tesseract
    [Tags]  tc06    TT
    [Setup]
    Check text in area
    Check text exists
    [Teardown]

*** Keywords ***
Start web-browser
     New Browser                 chromium  headless=false
     New Context                 viewport={'width': 800, 'height': 600}
     Set Browser Timeout         30000
     New Page                    ${URL}
     Wait For All Promises
Close web-browser
    Close Browser                CURRENT
