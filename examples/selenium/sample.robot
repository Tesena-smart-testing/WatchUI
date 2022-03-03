*** Settings ***
Library    SeleniumLibrary
# This import need to be changed into the correct path (now using last version WUI from this repo)
Library    ../../WatchUI/


*** Test Cases ***
Compare homapage with baseline
    Open Browser                https://www.google.com    chrome
    Capture Page Screenshot     baseline.png
    Compare Image               baseline.png              baselines/homepage.png    ssim=0.95
    Close Browser
