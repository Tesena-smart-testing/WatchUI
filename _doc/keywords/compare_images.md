---
title: Compare images

---
##### Describe
It compares two images from the two paths and, if there are differences, saves the image with the errors highlighted
in the folder which you choose. Default folder is ../Outputs

##### Arguments

<div class="table-responsive">

{: .table}
| Arguments | Documentation
|-
| path1 | path to the first image to be compared
| path2 | path to the second image to be compared
| save_folder | path, where you want to save images with highlighted differences (default: "../Outputs")
| ssim | threshold value in the interval (0, 1>. Tests are passed, if ssim value returned by keyword test functions is bigger than this (default: 1.0)
| image_format | Format for saving picture/screenshot (png, jpg etc.). Default is png

</div>

##### Example

###### Basic code:
```robotframework
*** Keywords ***
compare images   ${PATH1}  ${PATH2}
```

###### Full set up:
```robotframework
*** Keywords ***
compare images   ${PATH1}       ${PATH2}  save_folder=${SAVE_FOLDER}  ssim=${SSIM}  image_format=jpg
```
