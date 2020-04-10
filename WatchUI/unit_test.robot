*** Settings ***
Documentation    Suite description
Library          SeleniumLibrary
Library          OperatingSystem
Library          Screenshot
Library          WatchUI.py

*** Variables ***
${start_url}            https://www.tesena.com/contact-us/
${comparing_Screen}     https://www.czc.cz/
${browser}              Chrome
${basic_reso}           800  600

*** Test Cases ***
Compare two saved images
    [Tags]  compare_save_screen
    Compare images basic


Creating screens in differen resolutions
    [Tags]  resolution
    Create screens in 800 x 600 reso
    Create screens in 3 resolutions
    Create screens with full set up

Compare screen basic set up
    [Tags]  compare_screen
    Create screens from tesena
    Compare image with created screen
    Compare image with created screen full set up

Compare screen without some region
    [Tags]  cs_outregion
    Create screens from tesena
    Comparing screen without some area

*** Keywords ***
Compare images basic
    compare images   ./Img/forpres.png     ./Img/forpres.png

Compare images diff and full set upt
    compare images   ../Img/forpres.png     ./Img/forpres1.png  save_folder=./Tesena  ssim= 0.5

Create screens in 800 x 600 reso
    Open Browser                        ${start_url}      ${browser}
    create screens                      800  600
    Wait until created                  ./Outputs/screen800x600.png
    Close Browser

Create screens in 3 resolutions
    Open Browser                        ${start_url}      ${browser}
    create screens                      800  600    1280    800     1440    900
    Wait until created                  ./Outputs/screen800x600.png
    Wait until created                  ./Outputs/screen1280x800.png
    Wait until created                  ./Outputs/screen1440x900.png
    Close Browser

Create screens with full set up
    Open Browser                        ${start_url}      ${browser}
    create screens                      800  600    1280    800     save_folder=./newscreen    screen_name=resolution_is_
    Wait until created                  ./newscreen/resolution_is_800x600.png
    Wait until created                  ./newscreen/resolution_is_1280x800.png
    Close Browser

Create screens from tesena
    Open Browser                        ${start_url}      ${browser}
    create screens                      800  600
    Wait until created                  ./Outputs/screen800x600.png
    Close browser

Compare image with created screen
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800  600
    compare screen                     ./Outputs/screen800x600.png
    Close Browser

Compare image with created screen full set up
    Open Browser                        ${comparing_Screen}      ${browser}
    Set window size                     800  600
    compare screen                     ./Outputs/screen800x600.png     save_folder=./huf  ssim= 0.5
    Close Browser

Comparing screen without some area
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800  600
    compare screen without areas        ./Outputs/screen800x600.png    270  380  500  425  90  200  690  275
    Close Browser
