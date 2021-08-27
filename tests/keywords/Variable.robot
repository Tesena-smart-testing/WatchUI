*** Variables ***
# ---------------------------------------- Basic set up ----------------------------------------------------------------
${URL}                      https://www.tesena.com/contact-us/
${BROWSER}                  Chrome
${SF_OOUTPUTS}              ./Outputs
${SSIM1.0}                  1.0
${SSIM0.95}                 0.95
${SSIM0.5}                  0.5
@{reso}                     800  600
${screen800x600}            ./Outputs/screen.png
${FALSE}                    False

# ---------------------------------------- Compare 2 saved image ------------------------------------------------------
${1IMAGE}                   ../Img/forpres.png
${2IMAGE}                   ../Img/forpres1.png
${CS2_SFTESENA}             ../Tesena

# ---------------------------------------- Creating screens ------------------------------------------------------------
${SF_NEWSCREEN}             ./newscreen
${CS_SCREENNAME}            resolution_is_

# ---------------------------------------- Comparing screen ------------------------------------------------------------
${CS_SFOUTPUTS}             ./Outputs
${CS_NEWURL}                https://www.tesena.com/career/

# ---------------------------------------- Comparing screen without Area ------------------------------------------------------------
${CSWA_NEWURL}             https://www.czc.cz/
@{CSWA_BLACKSQUARE}        0  168  800  600
