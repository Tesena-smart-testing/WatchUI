---
title: Create Screens

---
##### Describe
Creates a screenshot on the screen.

Creates a screenshot on the screen, that corresponds to the specified resolution, so it is possible to create on one
page an infinite number of screens with different resolutions.

Default folder for saves screens: ../Outputs

<div class="callout-block callout-danger"><div class="icon-holder">*&nbsp;*{: .fa .fa-exclamation-triangle}
</div><div class="content">
{: .callout-title}
#### Warning

When you create one screen, name will be screen.png, but when you create more than one screen from same 4
page, name will be screen screen_name_width_height.png

</div></div>



##### Arguments

<div class="table-responsive">

{: .table}
| Arguments | Documentation
|-
| *resolution | The specified resolution in width and height format, you can enter as many as needed
| save_folder | path, where you want to save images with highlighted differences (default: "../Outputs")
| ssim | threshold value in the interval (0, 1>. Tests are passed, if ssim value returned by keyword test functions is bigger than this (default: 1.0)
| image_format | Format for saving picture/screenshot (png, jpg etc.). Default is png

</div>

##### Example

###### Basic code:
```robotframework
*** Keywords ***
Create screens  ${x1}   ${y1}
```

###### Full set up code:

```robotframework
*** Keywords ***
Create screens  ${x1}   ${y1}   ${x2}  ${y2}  ${x3}  ${y3}  save_folder=${SAVE_FOLDER}  ssim=${SSIM}  image_format=jpg
```