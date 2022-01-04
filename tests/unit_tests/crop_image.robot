*** Settings ***
Resource  settings/resources.robot


*** Test Cases ***
crop image check
    crop image  ${IMAGE_1}  20  20  100  100  save_folder=${result_files}/croped
    ${files}  List Files In Directory  ${result_files}/croped
    compare image  ${result_files}/croped/${files}[0]  ${croped_vzor}

crop image save as different format
    crop image  ${IMAGE_1}  20  20  100  100  save_folder=${result_files}/croped/jpg  image_format=${saved_changed_format}
    saved image format check  ${result_files}/croped/jpg
    ${files}  List Files In Directory  ${result_files}/croped/jpg
    compare image  ${croped_jpg_vzor}  ${result_files}/croped/jpg/${files}[0]  save_folder=${result_files}/croped/jpg
