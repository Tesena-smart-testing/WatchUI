*** Variables ***
${TESERACT_PATH}     /usr/bin/tesseract
${BASELINE_IMAGE}    assets/img.jpg
${IMAGE_1}           resource/data/forpres.png
${IMAGE_2}           resource/data/forpres1.png
${PDF_FILE}          assets/ok.pdf


*** Settings ***
Documentation    Suite description
Library          ../WatchUI/          outputs_folder=tests/outputs  tesseract_path=${TESERACT_PATH}

*** Test Cases ***
Compare Same Images
    Compare images    ${BASELINE_IMAGE}    ${BASELINE_IMAGE}    

Compare different Images
    [Tags]              1
    Compare images    ${IMAGE_1}    ${IMAGE_2}      ssim=0.5

Check Compare Screen Without Areas
    Compare screen without areas    ${BASELINE_IMAGE}    ${BASELINE_IMAGE}    0    0    100    100    125    125    250    250

Create Crop Image
    Crop Image    ${BASELINE_IMAGE}    10    10    20    20

Rotate Image For Fun
    Rotate Image    ${BASELINE_IMAGE}    rotate=1

PDF Convert To Image
    Pdf To Image    ${PDF_FILE}    zoom=5

Get Text From Some Area
    ${text_from_area}    Return Text From Area    ${PDF_FILE}    0    50    60    190    90
    Should Contain    ${text_from_area}             Územnímu pracovišti v, ve, pro 

Check If Text Exists
    Should Exist This Text    ${PDF_FILE}    0    Důvody

Get Text From Image
    [tags]            tesseract
    ${var}=           Image To String    ${BASELINE_IMAGE}  language=ces
    Should Contain    ${var}             Základní údaje o Teseně

Get Image Area On Text
    [tags]            tesseract
    ${var}=           Image Area On Text    ${BASELINE_IMAGE}    0    0    380    380
    Should Contain    ${var}                Intranet Delivery
