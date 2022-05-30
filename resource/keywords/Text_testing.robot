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

# ----------------------------------------- New test --------------------------------------- #
Create IMG
    Convert OK PDF to IMG
    Convert NOK PDF to IMG

Create and compare vysvetlivky
    Create Area from Vysvetlivky
    Check Vysvetlivky

Convert OK PDF to IMG
    pdf to image            ${OK_PDF}               name=${NAME_OK_PDF}

Convert NOK PDF to IMG
    pdf to image            ${NOK_PDF}              name=${NAME_NOK_PDF}

Find diff in PDF
    [Documentation]     Test to check that keyword will fail when pictures are different.
    ...     Status of test modified even the kw failed as we are testing it catch difference.
    ${status}=  Run Keyword And Return Status       Compare Images          ${PATH_TO_OK_IMG}       ${PATH_TO_NOK_IMG}
    Should Be True  '${status}'=='False'

Check words
    [Arguments]             ${WHAT_WE_SEARCH}       @{COO}
    ${Text_from_pdf}        Return text from area   ${NOK_PDF}              @{COO}
    should be true                                  '''${Text_from_pdf}''' == '''${WHAT_WE_SEARCH} '''

Create Area from Vysvetlivky
    pdf to image            ${OK_PDF}               name=${NAME_VYSVĚTLIVKY_OK_PDF}    number_page=7
    create area from image  @{COO_VYSVĚTLIVEK}      ${PATH_TO_VOK_IMG}      screen_name=${AREA_VYSVĚTLIVKY_OK_PDF}
    pdf to image            ${NOK_PDF}              name=${NAME_VYSVĚTLIVKY_NOK_PDF}    number_page=7
    create area from image  @{COO_VYSVĚTLIVEK}      ${PATH_TO_VNOK_IMG}     screen_name=${AREA_VYSVĚTLIVKY_NOK_PDF}

Check Vysvetlivky
    Compare Images          ${PATH_TO_VOK_AREA}     ${PATH_TO_VNOK_AREA}

Read text from image
    ${Text_from_area}       Image area on text      ${PATH_TO_NOK_IMG}      @{TEXT_COO_FOR_TESS}  language=ces
    should be true                                  '''${Text_from_area}''' == '''${CONTROLL_TEXT_FOR_TESS}'''



