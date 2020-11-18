---
title: Return text from area

---
##### Describe
Return text from area as string. It doesnt use tesseract, so its can be used on normally pdf without installed tesseract.

##### Arguments

<div class="table-responsive">

{: .table}
| Arguments | Documentation
|-
| path | path to the pdf
| page_number | PDF page number where we wanna search for text
| x1, y1, x2, y2 | coordinates where text is

</div>

##### Example

###### Basic code:
```robotframework
*** Keywords ***
Return text from area   ${PATH}  ${PAGE_NUMBER} ${x1}   ${y1}   ${x2}  ${y2}
```

###### Full set up:
```robotframework
*** Keywords ***
Return text from area   ${PATH}  ${PAGE_NUMBER} ${x1}   ${y1}   ${x2}  ${y2}
```
