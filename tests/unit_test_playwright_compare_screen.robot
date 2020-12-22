*** Settings ***
Library    Browser
Library    WatchUI    playwright    outputs_folder=${OUTPUTS_FOLDER}
Library    OperatingSystem

Resource   keywords/Variable.robot

Test Setup    Start web-browser
Test Teardown    Close web-browser

*** Variables ***
${OUTPUTS_FOLDER}           browser${/}Outputs
@{RESO}                     800  600

*** Test Cases ***
TC03.1 - Compare screen - image with created screen
    [Tags]  compare_screen  tc03  VT
    create screens          @{RESO}    save_folder=${OUTPUTS_FOLDER}
    Wait until created      ${OUTPUTS_FOLDER}${/}screen.png.png
    compare screen          ${OUTPUTS_FOLDER}${/}screen.png.png

*** Keywords ***
Start web-browser
     New Browser                 chromium  headless=false
     New Context                 viewport={'width': 800, 'height': 600}
     Set Browser Timeout         30000
     New Page                    ${URL}
     Wait For All Promises
Close web-browser
    Close Browser                CURRENT