*** Settings ***
Resource  tests_v2.robot

*** Keywords ***
Compare same images
    compare image   ${IMAGE_1}  ${IMAGE_1}

Compare different image
    [Arguments]  ${image_1}  ${image_2}
    register keyword to run on failure  none
    ${compare_different_image}  run keyword and return status    compare image   ${IMAGE_1}  ${IMAGE_2}
    run keyword if  ${compare_different_image}
    ...     fail
    ...     ELSE
    ...     no operation

compare screen without areas check
    compare screen without areas   ${image_1}  ${image_2}  30  15  1880  250  save_folder=${result_files}


rotate image check  #DOPLNIT DATA
    [Arguments]  ${rotation}
    rotate image  ${IMAGE_1}  screen_name=img_rotated_${rotation}  save_folder=${result_files}  rotate=${rotation}
    #pockat, nez se vytvori screen + dodelat cestu a vzory
    Compare different image  ${result_files}/img_rotated_${rotation}.png  ${IMAGE_1}
    compare image  ${result_files}/img_rotated_${rotation}.png  ${vzor_path}/img_rotated_vzor_${rotation}.png

pdf to image check  #DOPLNIT DATA
    [Arguments]  ${number_page}
    ${number_page-1}  evaluate  ${number_page} - 1
    pdf to image  ${PATH_TO_PDF}  save_folder=${result_files}  screen_name=pdf_screen_${number_page}  number_page=${number_page-1}
    compare image  ${result_files}/pdf_screen_${number_page}.png  ${vzor_path}/pdf_screen_vzor_${number_page}.png

return text from area check
    [Arguments]  ${number_page}  ${x1}  ${y1}  ${x2}  ${y2}
    ${number_page_evaluated}  evaluate  ${number_page} - 1
    ${returned_text}  return text from area  ${PATH_TO_PDF}  ${number_page_evaluated}  ${x1}  ${y1}  ${x2}  ${y2}
    should be equal as strings  ${returned_text}  ${RETURNED_TEXT_AREA_VZOR_${number_page}}


should exist this text check
    [Arguments]  ${number_page}  ${true/false}  ${checked_text}
    ${number_page_evaluated}  evaluate  ${number_page} - 1
    ${text_status}  should exist this text  ${PATH_TO_PDF}  ${number_page_evaluated}  ${checked_text}  #muze byt nejaky vzor z return text from area check
    should be true  "${text_status}" == "${true/false}"

image to string check  #mozna? nevime jak funguje
    ${image_to_string_value}  image to string  ${vzor_path}/image_to_string_vzor.png
    log to console  ${image_to_string_value}
    should contain  ${image_to_string_value}  hello there  ignore_case=True



image area on text check
    [Arguments]  ${image}  ${text}  ${x1}  ${y1}  ${x2}  ${y2}
    log to console  ${image}
    log to console  ${text}
    log to console  ${x1}
    log to console  ${y1}
    log to console  ${x2}
    log to console  ${y2}
    ${image_area_to_text_value}   image area on text  ${image}  ${x1}  ${y1}  ${x2}  ${y2}
    should be equal as strings  ${image_area_to_text_value}  ${text}  #DOPLNIT PROMENNE
