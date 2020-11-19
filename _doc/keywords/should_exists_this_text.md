---
title: Should exists this text

---
##### Describe
Returns True if search text is found in the page.

##### Arguments

<div class="table-responsive">

{: .table}
| Arguments | Documentation
|-
| path | Path to pdf
| page_number | PDF page number where we wanna check text
| text | Search text

</div>

##### Example

###### Basic code:
```robotframework
*** Keywords ***
Should exists this text   ${PATH}  ${PAGE_NUMBER} ${TEXT}
```

###### Full set up:
```robotframework
*** Keywords ***
Should exists this text   ${PATH}  ${PAGE_NUMBER} ${TEXT}
```
