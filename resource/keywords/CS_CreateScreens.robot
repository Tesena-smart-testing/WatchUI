*** Settings ***
Documentation    Keywords for creating Creating region

*** Keywords ***
Create screens in 800 x 600 reso
    create screens                      800  600    save_folder=${SF_OOUTPUTS}
    Wait until created                  ${screen800x600}

Create screens in 3 resolutions
    create screens                      800  600  1280  800  1440  900      save_folder=${SF_OOUTPUTS}
    Wait until created                  ${SF_OOUTPUTS}/screen800x600.png
    Wait until created                  ${SF_OOUTPUTS}/screen1280x800.png
    Wait until created                  ${SF_OOUTPUTS}/screen1440x900.png

Create screens with full set up
    create screens                      800  600    1280    800     save_folder=${SF_NEWSCREEN}    screen_name=${CS_SCREENNAME}
    Wait until created                  ${SF_NEWSCREEN}/${CS_SCREENNAME}800x600.png
    Wait until created                  ${SF_NEWSCREEN}/${CS_SCREENNAME}1280x800.png

Create screens with full set up: Format JPG
    create screens                      800  600    1280    800     save_folder=${SF_NEWSCREEN}    screen_name=${CS_SCREENNAME}     image_format=jpg
    Wait until created                  ${SF_NEWSCREEN}/${CS_SCREENNAME}800x600.jpg
    Wait until created                  ${SF_NEWSCREEN}/${CS_SCREENNAME}1280x800.jpg