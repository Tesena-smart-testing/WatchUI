*** Settings ***
Resource  ../../resources.robot
*** Test Cases ***
image area on text
    ${image}  set variable  ${vzor_path}/pdf_screen_vzor_1.png
    ${x1}  set variable  291
    ${y1}  set variable  316
    ${x2}  set variable  360
    ${y2}  set variable  330
    ${image_area_to_text_value}   image area on text  ${image}  ${x1}  ${y1}  ${x2}  ${y2}
    should be equal as strings  ${image_area_to_text_value}  ${RETURN_TEXT_FROM_AREA}  #DOPLNIT PROMENNE