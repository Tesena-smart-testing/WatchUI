---
title: Compare Screen Areas

---
##### Describe
Creates a cutout from the screen that matches the coordinates and then compares it to some cutout in the computer.

##### Arguments

<div class="table-responsive">

{: .table}
| Arguments | Documentation
|-
| x1 and y1 | x and y coordinates for the upper left corner of the square
| x2 and y2 | x and y coordinates for the bottom right corner of the square
| path1 | path to the first image to be compared
| save_folder | path, where you want to save images with highlighted differences (default: "../Outputs")
| ssim | threshold value in the interval (0, 1>. Tests are passed, if ssim value returned by keyword test functions is bigger than this (default: 1.0)
| image_format | Format for saving picture/screenshot (png, jpg etc.). Default format is png.

</div>

##### Example
```robotframework
*** Keywords ***
Compare screen areas                ${x1}   ${y1}   ${x2}  ${y2}     ${PATH1}
```
