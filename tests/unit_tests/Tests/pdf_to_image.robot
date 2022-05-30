*** Settings ***
Resource  ../../resources.robot
*** Test Cases ***
pdf to image check 1
    ${number_page}  set variable  1
    ${number_page-1}  evaluate  ${number_page} - 1
    pdf to image  ${PATH_TO_PDF}  save_folder=${result_files}  screen_name=pdf_screen_${number_page}  number_page=${number_page-1}
    compare image  ${result_files}/pdf_screen_${number_page}.png  ${vzor_path}/pdf_screen_vzor_${number_page}.png  save_folder=${result_files}/pdf

pdf to image check 2
    ${number_page}  set variable  2
    ${number_page-1}  evaluate  ${number_page} - 1
    pdf to image  ${PATH_TO_PDF}  save_folder=${result_files}  screen_name=pdf_screen_${number_page}  number_page=${number_page-1}
    compare image  ${result_files}/pdf_screen_${number_page}.png  ${vzor_path}/pdf_screen_vzor_${number_page}.png  save_folder=${result_files}/pdf