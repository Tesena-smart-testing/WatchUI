---
title: Basic Guide
sections:
  - Basic usage WatchUI in test
---

### Basic usage WatchUI in test
After installation we create new file test.robot with:

```robotframework
*** Settings ***

*** Variables ***

*** Test Cases ***

*** Keywords ***

```

Now we need to import under settings Selenium and WatchUI. Set up Test teardown for close browser and dont forget on Documentation.
```robotframework
*** Settings ***
Documentation   Suite description
Library         SeleniumLibrary
Library         Screenshot
Library         WatchUI.py
Test Teardown   Close All Browsers
```

Now we need create a simple variable for selenium. Becasue we wanna use Chrome as browser and Url will be tesla. We put to the code:
```robotframework
*** Variables ***
${start_url}        https://www.tesla.com/
${browser}          Chrome
```

Now we want to compare screenshot which we have in folder with webpage. So we create keywords for comparing screenshot and webpage. 

In keyword compare screen we must set up path to image which we want to compare with screen
```robotframework
*** Keywords ***
Screen compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    Sleep                               7
    Compare screen                      ./Outputs/screen800x600.png
```

Now we just create Test case:
```robotframework
*** Test Cases ***
Sample test
    NOK Screen compare
```

Ours file looks like:
```robotframework
*** Settings ***
Documentation   Suite description
Library         SeleniumLibrary
Library         Screenshot
Library         WatchUI.py
Test Teardown   Close All Browsers

*** Variables ***
${start_url}        https://www.tesla.com/
${browser}          Chrome

*** Test Cases ***
Sample test
    NOK Screen compare

*** Keywords ***
Screen compare
    Open Browser                        ${start_url}      ${browser}
    Set window size                     800     600
    Sleep                               7
    Compare screen                      ./Outputs/screen800x600.png
```

Now just start robot and thats all :-)