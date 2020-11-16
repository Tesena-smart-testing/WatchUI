*** Settings ***
Documentation    Keywords for testing text in image

*** Keywords ***
Convert PDF to IMG
    pdf to image    ${TT_path_to_pdf}   name=${TT_name_img}  save_folder=../Outputs/

From IMG to string
    ${Text_from_area}   Image area on text   ${TT_path_to_img}  @{TT_text_area_coo}     psm=10
     should be true                          '''${Text_from_area}''' == '''${TT_Should_be_text}'''

Check text in area
    ${Text_from_pdf}    Return text from area   ${TT_path_to_pdf}   0   50  60  190  90
    should be true                              '''${Text_from_pdf}''' == '''${TT_Should_be_text}'''

Check text exists
    ${Text_from_pdf}    Should exist this text  ${TT_path_to_pdf}   0   Dummy
    Should be true      ${Text_from_pdf} == True