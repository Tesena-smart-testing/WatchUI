*** Settings ***
Documentation                   Suite description
Library                         Screenshot
Library                         WatchUI
Library                         String
Library                         OperatingSystem

Resource                        resources_tests_v2.robot
*** Variables ***
${IMAGE_1}   ${vzor_path}/forpres.png
${IMAGE_2}   ${vzor_path}/forpres1.png
${IMAGE_SSIM_1}  ${vzor_path}/50.png
${IMAGE_SSIM_2}  ${vzor_path}/100.png
${croped_vzor}  ${vzor_path}/Croped_image_vzor.png
${croped_jpg_vzor}  ${vzor_path}/croped_image_jpg_vzor.jpg
${rotated_0_jpg_vzor}  ${vzor_path}/img_rotated_0_jpg_vzor.jpg

${RETURNED_TEXT_AREA_VZOR_1}  numer komisji${SPACE}${SPACE}
${RETURNED_TEXT_AREA_VZOR_2}  Bluetooth${SPACE}
${RETURN_TEXT_FROM_AREA}  ‘numer komisji

${PATH_TO_PDF}  resource/data/pdf_test.pdf

${CHECKED_TEXT_PDF}  numer komisji

${IMG_TO_STRING_CESTA}
${IMAGE_AREA_TO_TEXT_VZOR}
-------------------
${vzor_path}  resource/data
${result_files}  Results/files
${result_files_changed}  Results/files/changed_variables
${saved_changed_format}  jpg

${compare screen without areas_coordinates}  30  84  1880  79                 #30  84  160  220  1455  15  1880  79


	 numer komisji  !=
	 numer komisji