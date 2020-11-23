---
title: Import

---
##### Describe
Library can be imported either with default output folder and set lowest limit of difference between images (ssim), or you can provide your own values.

##### Arguments

<div class="table-responsive">

{: .table}
| Arguments | Documentation
|-
| outputs_folder |  path, where you want to save images with highlighted differences (default: "../Outputs")
| ssim_basic | threshold value in the interval (0, 1). Tests are passed, if ssim value returned by keyword test functions is bigger than this (default: 1.0)
| format_image |  Format for saving picture/screenshot (png, jpg etc.) Example: format_image=jpg (default: png)
| tesseract_path | path, where is tesseract.exe (Defaul folder is set up for windows settings: C:\Program Files\Tesseract-OCR\tesseract.exe)

</div>

##### Example

###### Basic code:
```robotframework
*** Settings ***
Library         WatchUI
```

###### Full set up:
```robotframework
*** Keywords ***
Library 	WatchUI 	outputs_folder=${OUTPUT_FOLDER} 	ssim_basic=${SSIM}  format_image=${PNG}  tesseract_path=${TESSERACT_PATH}
```
