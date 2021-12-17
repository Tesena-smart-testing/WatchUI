*** Settings ***
Documentation       Suite description
Library             ../WatchUI/   tesseract_path=/usr/bin/tesseract

*** Test Cases ***
Test title
    [Tags]    DEBUG
    Check Image
    Check compare screen without areas
    Create Crop Image
    Rotate Image for fun
    PDF convert to Image
    Get text from some area
    Check if text exists
    Get text from image
    Get Image area on text

*** Keywords ***
Check Image
    Compare image                           ../Tesena/img.jpg   ../Tesena/img.jpg

Check compare screen without areas
    Compare screen without areas            ../Tesena/img.jpg   ../Tesena/img.jpg    0  0  100  100

Create Crop Image
    Crop Image                              ../Tesena/img.jpg   10  10  20  20

Rotate Image for fun
    Rotate Image                            ../Tesena/img.jpg   rotate=1

PDF convert to Image
    pdf to image                            ../Tesena/ok.pdf

Get text from some area
    ${Text_from_area}                       return text from area   ../Tesena/ok.pdf  0     50  60  190  90
    log to console                          ${Text_from_area}

Check if text exists
    should exist this text                  ../Tesena/ok.pdf  0     Důvody

Get text from image
    ${var}=             image to string                         ../Tesena/img.jpg
    log to console      ${var}

Get Image area on text
    ${var}=             Image area on text                       ../Tesena/img.jpg     0  0  380  380
    log to console      ${var}