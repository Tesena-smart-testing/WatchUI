***Settings***

Library               WatchUI             outputs_folder=${IMAGES_STORAGE}/outputs
Library               Browser
Library               OperatingSystem

# with suite teardown cleaning the images, in the log these images will not
# be shown!
Suite Teardown        Remove Directory    ${IMAGES_STORAGE}   recursive=${True}

***Variables***

${IMAGES_STORAGE}     ${OUTPUTDIR}/tests/images

***Test Cases***

Compare Two Screenshots
    [Documentation]    Compares baseline image with actual image
    New Page           https://playwright.dev
    Take Screenshot    filename=${IMAGES_STORAGE}/baseline.png
    Reload
    Take Screenshot    filename=${IMAGES_STORAGE}/actual.png
    Compare Images     ${IMAGES_STORAGE}/baseline.png         ${IMAGES_STORAGE}/actual.png