*** Settings ***
Documentation    Keywords for comparing image in pc and screen in browser.

*** Keywords ***
Create screen from actual webpage
    create screens                      @{reso}    save_folder=${CS_SFOUTPUTS}
    Wait until created                  ./Outputs/screen800x600.png

Compare image with created screen
    Create screen from actual webpage
    compare screen                     ./Outputs/screen800x600.png

Compare image full set up
    Create screen from actual webpage
    compare screen                     ./Outputs/screen800x600.png     save_folder=${CS_SFOUTPUTS}  ssim=${SSIM1.0}

Compare diff image
    Create screen from actual webpage
    Go to                               ${CS_NEWURL}
    compare screen                     ./Outputs/screen800x600.png     save_folder=${CS_SFOUTPUTS}  ssim=${SSIM0.5}
