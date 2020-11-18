---
title: Rotate image

---
##### Describe
Rotate image.

##### Arguments

<div class="table-responsive">

{: .table}
| Arguments | Documentation
|-
| path | Path to the image, which we wanna rotate.
| rotate | How we want to rotate the image. 0 = 90degrees Clockwise, 1 = 90degrees Counter clockwise and 2= 180degrees
| screen_name | Name of the new image. Default is rotate_screen.
| save_folder | path, where you want to save images with highlighted differences (default: "../Outputs")
| image_format | Format for saving picture/screenshot (png, jpg etc.). Default is png

</div>

##### Example

###### Basic code:
```robotframework
*** Keywords ***
Rotate image   ${PATH}  ${ROTATE}
```

###### Full set up:
```robotframework
*** Keywords ***
Rotate image   ${PATH}  ${ROTATE}  screen_name=${SCREEN_NAME}  save_folder=${SAVE_FOLDER}  image_format=jpg
```
