---
title: Image area on text

---
##### Describe
Takes text from the coordinates on the image and returns list.

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
| *coordinates | coordinates where text is located. At least 4 (x1, y1, x2, y2)
| oem | Engine Mode (Settings from tesseract)
| PSM | Page Segmentation Mode (Settings from tesseract)
| language | The Language we wanna read file
| path_to_tesseract | Path to root folder with tesseract.exe

</div>

##### Example

###### Basic code:
```robotframework
*** Keywords ***
Image area on text   ${PATH1}  ${x1}   ${y1}   ${x2}  ${y2}
```

###### Full set up:
```robotframework
*** Keywords ***
compare images   ${PATH1}  ${x1}   ${y1}   ${x2}  ${y2}  oem=${OEM}  psm=${PSM} language=${LANG}  compare images   ${PATH1}  ${x1}   ${y1}   ${x2}  ${y2}  oem=${OEM}  psm=${PSM} language=${LANG}

```
