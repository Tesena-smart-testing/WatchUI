---
title: Image to string

---
##### Describe
Keyword takes all the text it finds on the page and returns it as a string.

<div class="callout-block callout-danger"><div class="icon-holder">*&nbsp;*{: .fa .fa-exclamation-triangle}
</div><div class="content">
{: .callout-title}
#### Be wary of tesseract

For proper functionality you must install tesseract-ocr. [Link for installation tesseract](/WatchUI/start.html#install-tesseract).
Basic guide for using here.

</div></div>

##### Arguments

<div class="table-responsive">

{: .table}
| Arguments | Documentation
|-
| path | path to the image, which we wanna read
| oem | Engine Mode (Settings from tesseract)
| PSM | Page Segmentation Mode (Settings from tesseract)
| language | The Language we wanna read file
| path_to_tesseract | Path to root folder with tesseract.exe

</div>

##### Example

###### Basic code:
```robotframework
*** Keywords ***
Image to string   ${PATH1}  path_to_tesseract=${PATH_TO TESERACT}
```

###### Full set up:
```robotframework
*** Keywords ***
Image to string   ${PATH1}  path_to_tesseract=${PATH_TO TESERACT}  oem=${OEM}  psm=${PSM} language=${LANG}
```
