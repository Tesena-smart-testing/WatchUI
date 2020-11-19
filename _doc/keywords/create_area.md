---
title: Create area

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

###### Basic code:
You can create area imagine as:
```robotframework
*** Keywords ***
Create area  ${x1}   ${y1}   ${x2}  ${y2}
```

Its same as:
```robotframework
*** Keywords ***
Create area  0   0   300  200
```
This code creates cutout from coordinates (0,0,300,200)

###### Full set up code:

```robotframework
*** Keywords ***
Create area  ${x1}   ${y1}   ${x2}  ${y2}  save_folder=${SAVE_FOLDER}  ssim=${SSIM}  image_format=jpg
```