*** Settings ***
Documentation       Suite description
Library             WatchUI

*** Test Cases ***
Test title
    [Tags]    DEBUG
    Check Image

*** Keywords ***
Check Image
    Compare image   ../Tesena/img.jpg   ../Tesena/img.jpg