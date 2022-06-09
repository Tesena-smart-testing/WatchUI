*** Settings ***
Resource  ../../resources.robot
*** Test Cases ***
rotate image check 0
    ${rotation}  set variable  0
    rotate image  ${IMAGE_1}  screen_name=img_rotated_${rotation}  save_folder=${result_files}/rotation   rotate=${rotation}
    Compare different image arg  ${result_files}/rotation/img_rotated_${rotation}.png  ${IMAGE_1}
    compare image  ${result_files}/rotation/img_rotated_${rotation}.png  ${vzor_path}/img_rotated_vzor_${rotation}.png

rotate image check 1
    ${rotation}  set variable  1
    rotate image  ${IMAGE_1}  screen_name=img_rotated_${rotation}  save_folder=${result_files}/rotation  rotate=${rotation}
    Compare different image arg  ${result_files}/rotation/img_rotated_${rotation}.png  ${IMAGE_1}
    compare image  ${result_files}/rotation/img_rotated_${rotation}.png  ${vzor_path}/img_rotated_vzor_${rotation}.png

rotate image check 2
    ${rotation}  set variable  2
    rotate image  ${IMAGE_1}  screen_name=img_rotated_${rotation}  save_folder=${result_files}/rotation  rotate=${rotation}
    Compare different image arg  ${result_files}/rotation/img_rotated_${rotation}.png  ${IMAGE_1}
    compare image  ${result_files}/rotation/img_rotated_${rotation}.png  ${vzor_path}/img_rotated_vzor_${rotation}.png

rotate image save as different format
    ${rotation}  set variable  0
    rotate image  ${IMAGE_1}  screen_name=img_rotated_${rotation}  save_folder=${result_files}/rotation/jpg  rotate=${rotation}  image_format=${saved_changed_format}
    ${files}  List Files In Directory  ${result_files}/rotation/jpg
    compare image  ${rotated_0_jpg_vzor}  ${result_files}/rotation/jpg/${files}[0]  save_folder=${result_files}/rotation