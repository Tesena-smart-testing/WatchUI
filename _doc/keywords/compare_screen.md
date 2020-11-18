---
title: Compare screen

---
##### Describe
Compares the already saved image with the screen that is on the screen. If there is a difference, it saves the
highlighted image to the: ../Outputs

##### Arguments

<div class="table-responsive">

{: .table}
| Arguments | Documentation
|-
| path1 | path to the first image to be compared
| save_folder | path, where you want to save images with highlighted differences (default: "../Outputs")
| ssim | threshold value in the interval (0, 1>. Tests are passed, if ssim value returned by keyword test functions is bigger than this (default: 1.0)
| image_format | Format for saving picture/screenshot (png, jpg etc.). Default is png

</div>

##### Example

###### Basic code:
```robotframework
*** Keywords ***
compare screen  ${PATH1} 
```

###### Full set up:
```robotframework
*** Keywords ***
compare screen  ${PATH1}  save_folder=${SAVE_FOLDER}  ssim=${SSIM}  image_format=jpg
```
