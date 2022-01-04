*** Settings ***
Resource  settings/resources.robot


*** Test Cases ***
image to string check
    ${image_to_string_value}  image to string  ${vzor_path}/image_to_string_vzor.png
    log to console  ${image_to_string_value}
    should contain  ${image_to_string_value}  hello there  ignore_case=True