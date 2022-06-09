*** Settings ***
Resource  ../../resources.robot
*** Test Cases ***
should exist this text check 1
    ${number_page}  set variable  1
    ${true/false}  set variable  True
    ${checked_text}  set variable  ${checked_text_pdf}

    ${number_page_evaluated}  evaluate  ${number_page} - 1
    ${text_status}  should exist this text  ${PATH_TO_PDF}  ${number_page_evaluated}  ${checked_text}  #muze byt nejaky vzor z return text from area check
    should be true  "${text_status}" == "${true/false}"

should exist this text check 2
    ${number_page}  set variable  2
    ${true/false}  set variable  False
    ${checked_text}  set variable  ${checked_text_pdf}

    ${number_page_evaluated}  evaluate  ${number_page} - 1
    ${text_status}  should exist this text  ${PATH_TO_PDF}  ${number_page_evaluated}  ${checked_text}  #muze byt nejaky vzor z return text from area check
    should be true  "${text_status}" == "${true/false}"