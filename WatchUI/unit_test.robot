*** Settings ***
Documentation    Suite description
Library          SeleniumLibrary
Library          Screenshot
Library          WatchUI.py

*** Variables ***
${start_url}        https://www.alza.cz/
${new_url}          https://www.czc.cz/
${browser}          Chrome
${element}          id=logo
@{loc}              0   0   30   40

*** Test Cases ***

*** Keywords ***
Two images compare
    compare images                       ./Img/forpres.PNG    ./Img/forpres1.png    ./compare

Screen compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     1280     800
    sleep                               5
    compare screen                      ../Create rescreens/rescreen_1280x800.png

Making compare area
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    sleep                               2
    create area                         0   0   300  400

Area Compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    sleep                               2
    compare screen areas                0   0   300     400     ../img/test.png

Areas Compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     1280     800
    sleep                               2
    compare screen without areas        ../Create rescreens/rescreen_1280x800.png   303  236  1113  476

Making rescreens
    Open Browser                        ${start_url}      ${browser}
    create screens                      800  600    1280    800     1440    900

Area compare with info
    Open Browser                        ${start_url}    ${browser}
    Set window size                     1280     800
    sleep                               4
    compare screen get information      ../Create rescreens/rescreen_1280x800.png
