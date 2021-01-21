*** Variables ***
# ---------------------------------------- Basic set up ----------------------------------------------------------------
${URL}                          https://www.tesena.com/contact-us/
${BROWSER}                      Chrome
${SF_OOUTPUTS}                  ../Outputs
${SSIM1.0}                      1.0
${SSIM0.95}                     0.95
${SSIM0.5}                      0.5
@{reso}                         800  600
${screen800x600}                ../Outputs/screen.png
${FALSE}                        False

# ---------------------------------------- Compare 2 saved image ------------------------------------------------------
${1IMAGE}                       ../Img/forpres.png
${2IMAGE}                       ../Img/forpres1.png
${CS2_SFTESENA}                 ../Tesena

# ---------------------------------------- Creating screens ------------------------------------------------------------
${SF_NEWSCREEN}                 ../newscreen
${CS_SCREENNAME}                resolution_is_

# ---------------------------------------- Comparing screen ------------------------------------------------------------
${CS_SFOUTPUTS}                 ../Outputs
${CS_NEWURL}                    https://www.tesena.com/career/

# ---------------------------------------- Comparing screen without Area ------------------------------------------------------------
${CSWA_NEWURL}                  https://www.alza.cz/
@{CSWA_BLACKSQUARE}             0  168  800  600

# ---------------------------------------- Text testing ------------------------------------------------------------
${TT_path_to_pdf}               ../Img/dummy.pdf
${TT_name_img}                  pdfInPng
${TT_path_to_img}               ../Outputs/${TT_name_img}.png
@{TT_text_area_coo}             0    0   179     83
${TT_Should_be_text}            Dummy PDF file
#------------------------------------------ New PDF file --------------------------------------------------------------
${OK_PDF}                       ../Img/ok.pdf
${NOK_PDF}                      ../Img/nok.pdf

${NAME_OK_PDF}                  Ok
${PATH_TO_OK_IMG}               ../Outputs/${NAME_OK_PDF}_0.png
${NAME_NOK_PDF}                 nok
${PATH_TO_NOK_IMG}              ../Outputs/${NAME_NOK_PDF}_0.png

@{TEXT_COO}                     0  240  290   393  318  # First is number page, after x1,y1,x2,y2
${CONTROLL_TEXT}                P Ř I Z N Á N Í

${CONTROLL_TEXT_FOR_TESS}       PŘIZNÁNÍ
@{TEXT_COO_FOR_TESS}            727  860   1200  945

${NAME_VYSVĚTLIVKY_OK_PDF}      vOk
${NAME_VYSVĚTLIVKY_NOK_PDF}     vNok
${PATH_TO_VOK_IMG}              ../Outputs/${NAME_VYSVĚTLIVKY_OK_PDF}.png
${PATH_TO_VNOK_IMG}             ../Outputs/${NAME_VYSVĚTLIVKY_NOK_PDF}.png

@{COO_VYSVĚTLIVEK}              60  1930    1580    2431
${AREA_VYSVĚTLIVKY_OK_PDF}      vysOk
${AREA_VYSVĚTLIVKY_NOK_PDF}     vysNok

${PATH_TO_VOK_AREA}             ../Outputs/${AREA_VYSVĚTLIVKY_OK_PDF}.png
${PATH_TO_VNOK_AREA}            ../Outputs/${AREA_VYSVĚTLIVKY_NOK_PDF}.png

