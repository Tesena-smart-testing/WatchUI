*** Settings ***
Documentation   Suite description
Library         SeleniumLibrary
Library         Screenshot
Library         WatchUi
Test Teardown   Close All Browsers

*** Variables ***
${start_url}        https://www.tesla.com/
${browser}          Chrome
@{loc}              0   0   30   40

*** Test Cases ***
Sample test
    Create screenshots
    Two images compare
    # NOK Screen compare
    Create region
    # NOK Area Compare
    Comparing screen without some region
    Area compare with info


*** Keywords ***
Two images compare
    Compare images                      ./Outputs/screen800x600.png    ./Outputs/screen800x600.png    ./Outputs

Screen compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    Sleep                               7
    Compare screen                      ./Outputs/screen800x600.png  save_folder=Outputs

Create region
    Open Browser                        ${start_url}      ${browser}
    Set window size                     1280     800
    Sleep                               2
    Create area                         0   0   300  200  save_folder=Outputs

Area Compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     1280     800
    Sleep                               2
    Compare screen areas                0   0   1179     704     Outputs/screen800x600.png  save_folder=Outputs

Comparing screen without some region
    Open Browser                        ${start_url}      ${browser}
    Set window size                     1280     800
    Sleep                               2
    Compare screen without areas        Outputs/screen1280x800.png   120  100  1800  500  save_folder=Outputs

Create screenshots
    Open Browser                        ${start_url}      ${browser}
    Create screens                       800  600  1280  800  1440  900  save_folder=Outputs  screen_name=screen

Area compare with info
    Open Browser                        ${start_url}    ${browser}
    Set window size                     800     600
    Sleep                               7
    Compare screen get information      1c.png  save_folder=Outputs  folder_csv=Outputs
