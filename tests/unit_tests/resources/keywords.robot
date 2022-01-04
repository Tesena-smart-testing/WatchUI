*** Settings ***
Resource            ../settings/resources.robot
*** Keywords ***

saved image format check
    [Arguments]  ${result_files_changed_var}
    ${files}  List Files In Directory  ${result_files_changed_var}
    ${files_splited}  split string  ${files}[0]  .
    should contain  ${files_splited}[2]  jpg  ignore_case=True

Compare different image arg
    [Arguments]  ${IMAGE_ARG_1}  ${IMAGE_ARG_2}
    ${difference_status}  run keyword and return status    compare image   ${IMAGE_ARG_1}  ${IMAGE_ARG_2}
    run keyword if  ${difference_status}
    ...     fail
    ...     ELSE
    ...     no operation