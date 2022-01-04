*** Settings ***
Resource  settings/resources.robot


*** Test Cases ***
image area on text
 #   [Arguments]  ${image}  ${text}  ${x1}  ${y1}  ${x2}  ${y2}
    ${image}  set variable  ${vzor_path}/pdf_screen_vzor_1.png
    ${text}  set variable  ${RETURNED_TEXT_AREA_VZOR_1}
    ${x1}  set variable  291
    ${y1}  set variable  316
    ${x2}  set variable  360
    ${y2}  set variable  330
    ${image_area_to_text_value}   image area on text  ${image}  ${x1}  ${y1}  ${x2}  ${y2}
    should be equal as strings  ${image_area_to_text_value}  ${text}  #DOPLNIT PROMENNE