*** Settings ***
Documentation    Keyword for comparing screen without some region

*** Keywords ***
Comparing screen without some area: PNG Format
    Go to                               ${CSWA_NEWURL}
    create screens                      800  600     save_folder=${SF_OOUTPUTS}
    compare screen without areas        ${screen800x600}      @{CSWA_BLACKSQUARE}    ssim=${SSIM0.95}

Comparing screen without some area: JPG Format
    Go to                               ${CSWA_NEWURL}
    create screens                      800  600     save_folder=${SF_OOUTPUTS}
    compare screen without areas        ${screen800x600}      @{CSWA_BLACKSQUARE}    ssim=${SSIM0.95}  image_format=jpg
