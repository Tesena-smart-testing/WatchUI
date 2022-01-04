*** Settings ***
Resource  settings/resources.robot


*** Test Cases ***
Compare same images
    compare image   ${IMAGE_1}  ${IMAGE_1}

Compare different image
    ${difference_status}  run keyword and return status    compare image   ${IMAGE_1}  ${IMAGE_2}
    run keyword if  ${difference_status}
    ...     fail
    ...     ELSE
    ...     no operation

compare image save to folder
    ${difference_status}  run keyword and return status    compare image   ${IMAGE_1}  ${IMAGE_2}  save_folder=${result_files}/compare_image
    run keyword if  ${difference_status}
    ...     fail
    ...     ELSE
    ...     no operation

compare image ssim 90 pass
    compare image  ${IMAGE_1}  ${IMAGE_2}  save_folder=${result_files}/compare_image  ssim=0.9

compare image ssim 90 fail
    ${difference_status}  run keyword and return status  compare image  ${IMAGE_SSIM_1}  ${IMAGE_SSIM_2}  save_folder=${result_files}/compare_image  ssim=0.9
    run keyword if  ${difference_status}
    ...     fail
    ...     ELSE
    ...     no operation

compare image ssim 30 pass
    compare image  ${IMAGE_SSIM_1}  ${IMAGE_SSIM_2}  save_folder=${result_files}/compare_image  ssim=0.3

compare image ssim 30 fail
    ${difference_status}  run keyword and return status  compare image  ${IMAGE_SSIM_1}  ${IMAGE_1}  save_folder=${result_files}/compare_image  ssim=0.3
    run keyword if  ${difference_status}
    ...     fail
    ...     ELSE
    ...     no operation


compare image save as different format
    compare image  ${IMAGE_1}  ${IMAGE_2}   save_folder=${result_files}/compare_image/jpg  ssim=0.9  image_format=${saved_changed_format}
    saved image format check  ${result_files}/compare_image/jpg