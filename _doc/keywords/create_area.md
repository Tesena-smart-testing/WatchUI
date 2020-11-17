---
title: Create area
sections:
  - Describe
  - Arguments
  - Example
---
##### Describe
Creates a cut-out from the screen that is on screen and saves it in the folder: ../Outputs

##### Arguments

<div class="table-responsive">

{: .table}
| Arguments | Documentation
|-
| x1 and y1 | x and y coordinates for the upper left corner of the square
| x2 and y2 | x and y coordinates for the bottom right corner of the square
| save_folder | path, where you want to save images with highlighted differences (default: "../Outputs")
| screen_name | Name of the created image from area
| image_format | Format for saving picture/screenshot (png, jpg etc.). Default is png

</div>

##### Example
You can create area imagine as:
```robotframework
*** Keywords ***
Create area  ${x1}   ${y1}   ${x2}  ${y2}  save_folder=Outputs
```

Its same as:
```robotframework
*** Keywords ***
Create area  0   0   300  200  save_folder=Outputs
```
Thise code creates cutout from coordinates (0,0,300,200)