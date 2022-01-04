*** Settings ***
Documentation                   Suite description
Library                         Screenshot
Library                         WatchUI
Library                         String
Library                         OperatingSystem

Resource                        resources_tests_v2.robot
Resource                        resources.robot


Test Setup                      Start web-browser
#Test Teardown                   Close web-browser

#   robot -d Results tests/tests_v2.robot
#   robot -d Results -i fix tests/tests_v2.robot

#stalo by za to vsude pridat screen name
#neumi porovnat obrazek 2 rozdilnuch formatu, i kdyz jsou stejne
*** Test Cases ***



#compare_image_test  #ok
#    compare same images
#    compare different image  ${IMAGE_1}  ${IMAGE_2}
#    compare image save to folder
#    compare image ssim 90 pass
#    compare image ssim 90 fail
#    compare image ssim 30 pass
#    compare image ssim 30 fail
#    compare image save as different format

#compare_screen_without_areas_test  #NOK #nejde zadat vicero souradnic
#    compare screen without areas check

#crop_image_test
#    crop image check
#    crop image save as different format
#
#rotate_image_test  # OK
#    rotate image check  # 0  #rotation
#    rotate image check  # 1  #rotation
#    rotate image check  # 2  #rotation
#    rotate image save folder change  # 0
#    rotate image save as different format  # 0
#
#pdf_to_image_test  #ok
#    pdf to image check  1  #PDF page
#    pdf to image check  2  #PDF page

return_text_from_area_test  #NOK - problem s mezerama za slovem
    return text from area check  1  291  315  360  330  #page number, x1, y1, x2, y2
    return text from area check  2  231  145  520  205  #page number, x1, y1, x2, y2

#should_exist_this_text_test  #OK
#    should exist this text check  1  True  ${checked_text_pdf}
#    should exist this text check  2  False  ${checked_text_pdf}

#image_to_string_test  #ok
#    image to string check

image_area_on_text_test  #NOK  -vraci nejake divne hodnoty
    image area on text check  ${vzor_path}/pdf_screen_vzor_1.png  ${RETURNED_TEXT_AREA_VZOR_1}  291  315  360  330  #image, text, x1, y1, x2, y2
