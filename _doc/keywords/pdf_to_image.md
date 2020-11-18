---
title: Pdf to image

---
##### Describe
Change PDF to Image. Default folder for saves image is: ../Outputs

##### Arguments

<div class="table-responsive">

{: .table}
| Arguments | Documentation
|-
| path | Path to the pdf, which we wanna change to image.
| number_page | PDF´s page number, which we change into image. Default is 0
| name | Name of the image, we going to creating. Default is img.
| save_folder | path, where you want to save images with highlighted differences (default: "../Outputs")

</div>

##### Example

###### Basic code:
```robotframework
*** Keywords ***
Pdf to image   ${PATH}
```

###### Full set up:
```robotframework
*** Keywords ***
Pdf to image   ${PATH}  ${NUMBER_PAGE}  ${NAME}  ${SAVE_FOLDER}
```
