*** Settings ***
Resource  ../../resources.robot
*** Test Cases ***
return text from area check 1
    ${number_page}  set variable  1
    ${x1}  set variable  30
    ${y1}  set variable  70
    ${x2}  set variable  280
    ${y2}  set variable  100
    ${number_page_evaluated}  evaluate  ${number_page} - 1
    ${returned_text}  return text from area  ${PATH_TO_PDF}  ${number_page_evaluated}  ${x1}  ${y1}  ${x2}  ${y2}
    should be equal as strings  ${returned_text}  ${RETURNED_TEXT_AREA_VZOR_${number_page}}

return text from area check 2
    ${number_page}  set variable  2
    ${x1}  set variable  231
    ${y1}  set variable  145
    ${x2}  set variable  522
    ${y2}  set variable  205
    ${number_page_evaluated}  evaluate  ${number_page} - 1
    ${returned_text}  return text from area  ${PATH_TO_PDF}  ${number_page_evaluated}  ${x1}  ${y1}  ${x2}  ${y2}
    should be equal as strings  ${returned_text}  ${RETURNED_TEXT_AREA_VZOR_${number_page}}