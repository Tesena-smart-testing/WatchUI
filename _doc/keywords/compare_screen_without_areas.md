---
title: Compare Screen Without Areas

---
##### Describe
Compares two images, some parts of which will be ignored. Which parts then determine the coordinates.

One or more parts can be discarded from the comparison.
##### Arguments

<div class="table-responsive">

{: .table}
| Arguments | Documentation
|-
| path1 | path to the image, which to be compared
| x1 and y1 | x and y coordinates for the upper left corner of the square
| x2 and y2 | x and y coordinates for the bottom right corner of the square
| save_folder | path, where you want to save images with highlighted differences (default: "../Outputs")
| ssim | threshold value in the interval (0, 1>. Tests are passed, if ssim value returned by keyword test functions is bigger than this (default: 1.0)
| image_format | Format for saving picture/screenshot (png, jpg etc.). Default folder is png

</div>

##### Example
Basic code is:
```robotframework
*** Keywords ***
compare images   ${PATH1}   ${x1}   ${y1}   ${x2}  ${y2}
```

For more discarded area:
```robotframework
*** Keywords ***
compare images   ${PATH1}   ${x1}   ${y1}   ${x2}  ${y2}  ${x1}   ${y1}   ${x2}  ${y2}  ${x1}   ${y1}   ${x2}  ${y2}
```
How it looks like after compare:
<div class="screenshot-holder">
   <a href="./img/logscreen.png" data-title="LogScreen" data-toggle="lightbox"><img class="img-responsive" src="./img/logscreen.png" alt="screenshot" /></a>
   <a class="mask" href="./img/logscreen.png" data-title="LogScreen" data-toggle="lightbox"><i class="icon fa fa-search-plus"></i></a>
  </div>
 </div>