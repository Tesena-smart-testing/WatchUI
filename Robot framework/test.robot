*** Settings ***
Documentation    Suite description
Library          SeleniumLibrary
Library          Screenshot
Library          ../WatchUI/WatchUI.py


*** Variables ***
${start_url}        https://www.alza.cz/
${new_url}          https://www.czc.cz/
${browser}          Chrome
${element}          id=logo
@{loc}              0   0   30   40

*** Test Cases ***
Test
    # Two images compare
    # Screen compare
    # Create  region
    # Area Compare
    # Comparing screen without some region
    # Making rescreens
    # Area compare with info


*** Keywords ***
Two images compare
    compare two image                   ../Save Image/testscreen.png    ../img.png    ../try

Screen compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    sleep                               7
    compare screen                      ../Create_screens/screen800x600.png

Making compare area
    Open Browser                        ${start_url}      ${browser}
    Set window size                     1280     800
    sleep                               2
    Create area                         0   0   300  400

Area Compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     1280     800
    sleep                               2
    compare screen areas                0   0   300     400     ../Img/test.png

Comparing screen without some region
    Open Browser                        ${start_url}      ${browser}
    Set window size                     1280     800
    sleep                               2
    compare screen without areas        ../Img/test1.png   255  224  1153  583

Making rescreens
    Open Browser                        ${start_url}      ${browser}
    Create screens                       800  600    1280    800     1440    900  screen_name=Alza

Area compare with info
    Open Browser                        ${start_url}    ${browser}
    Set window size                     800     600
    sleep                               7
    compare screen get information      1c.png
