*** Settings ***
Documentation    Keyword for comparing screen without some region

*** Keywords ***
Comparing screen without some area
    Go to                               ${CSWA_NEWURL}
    create screens                      800  600     save_folder=${SF_OOUTPUTS}
    compare screen without areas        ./Outputs/screen800x600.png     @{CSWA_BLACKSQUARE}    ssim=${SSIM0.95}
