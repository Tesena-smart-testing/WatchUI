*** Settings ***
Documentation    Keywords for compare two saved image in pc

*** Keywords ***
Compare 2 same images
    compare images   ${1IMAGE}       ${2IMAGE}

Compare images SSIM 0.5
    compare images   ${1IMAGE}       ${2IMAGE}  save_folder=${CS2_SFTESENA}  ssim=${SSIM0.5}  image_format=jpg

Compare images SSIM 0.5: JPG Format
    compare images   ${1IMAGE}       ${2IMAGE}  save_folder=${CS2_SFTESENA}  ssim=${SSIM0.5}  image_format=jpg