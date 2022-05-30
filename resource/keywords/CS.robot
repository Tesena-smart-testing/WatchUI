*** Settings ***
Documentation    Keywords for comparing image in pc and screen in browser.


*** Keywords ***
Create screen from actual webpage
    create screens                      @{reso}    save_folder=${CS_SFOUTPUTS}
    Wait until created                  ${screen800x600}

Compare image with created screen
    Create screen from actual webpage
    compare screen                      ${screen800x600}

Compare image full set up
    Create screen from actual webpage
    compare screen                      ${screen800x600}      save_folder=${CS_SFOUTPUTS}  ssim=${SSIM1.0}

Compare diff image ssim 0.5
    Create screen from actual webpage
    Go to                               ${CS_NEWURL}
    compare screen                      ${screen800x600}      save_folder=${CS_SFOUTPUTS}  ssim=${SSIM0.5}
    Go to                               ${URL}

Compare diff image ssim 1.0
    Create screen from actual webpage
    Go to                               ${CS_NEWURL}
    ${failed}=                           Run Keyword And Return Status     compare screen    ${screen800x600}      save_folder=${CS_SFOUTPUTS}  ssim=${SSIM1.0}
    Should be true                      '''${FALSE}''' == '''${false}'''

Compare image without ssim set up
    Create screen from actual webpage
    compare screen                      ${screen800x600}    save_folder=${CS_SFOUTPUTS}

Compare image without full set up
    Create screen from actual webpage
    ${false}=                          Run Keyword And Return Status       compare screen  asdf
    Should be true                      '''${FALSE}''' == '''${false}'''

Compare diff image image format JPG
    Create screen from actual webpage
    Go to                               ${CS_NEWURL}
    ${false}=                           Run Keyword And Return Status       compare screen       ${screen800x600}      save_folder=${CS_SFOUTPUTS}  ssim=${SSIM1.0}  image_format=jpg
    Should be true                      '''${FALSE}''' == '''${false}'''
    Go to                               ${URL}
