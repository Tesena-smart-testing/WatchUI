*** Settings ***
Documentation    Suite description
Library          SeleniumLibrary
Library          Screenshot
Library          ../Watchmen/robotframework.py


*** Variables ***
${start_url}        https://www.alza.cz/
${new_url}          https://www.czc.cz/
${browser}          Chrome
${element}          id=logo
@{loc}              0   0   30   40

*** Test Cases ***
Test
    # Two images compare
    Screen compare
    # Making compare area
    # Area Compare
    # Areas Compare
    # Making rescreens
    # Area compare with info


*** Keywords ***
Two images compare
    compare two image                   ../Save Image/testscreen.png    ../img.png    ../try

Screen compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    sleep                               7
    compare screen                      ../Create rescreens/rescreen_800x600.png

Making compare area
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    sleep                               2
    compare making area                 0   0   300  400

Area Compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    sleep                               2
    compare screen area                 0   0   300     400     ../img/test.png

Areas Compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    sleep                               2
    compare screen without areas        ../img/test1.png   255  224  1153  583

Making rescreens
    Open Browser                        ${start_url}      ${browser}
    compare making rescreens            800  600    1280    800     1440    900

Area compare with info
    Open Browser                        ${start_url}    ${browser}
    Set window size                     800     600
    sleep                               7
    compare screen get information      1c.png
