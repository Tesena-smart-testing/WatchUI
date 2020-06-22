*** Settings ***
Documentation    Keyword for creating area

*** Keywords ***
Create area 200 x 500: basic
        Go to                               ${CSWA_NEWURL}
        create area                         0  0  200  500  save_folder=${SF_OOUTPUTS}   screen_name=screen1
        Should exist                        ${SF_OOUTPUTS}/screen1.png


Create area 200 x 500: full set up
        Go to                               ${CSWA_NEWURL}
        create area                         0  0  200  500  save_folder=${SF_OOUTPUTS}   screen_name=screen1  image_format=jpg
        Should exist                        ${SF_OOUTPUTS}/screen1.jpg