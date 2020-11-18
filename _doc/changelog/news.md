---
title: News
sections:
    - 1.0.7
    - 1.0.6
    - 1.0.5
    - 1.0.0
    - 0.17.8
    - 0.17.2
    - 0.16.4
    - 0.14.1
---


# Changelog

All notable changes to this project will be documented in this file.


### 1.0.7 - 2020-11-18

#### Added

- New documentation
- New actions
- New unit test

#### Changed
- Repair comments in code
- 

### 1.0.6 - 2020-09-11

#### Added

- New keyword for works with PDF and tesseract
- New unit test
- add __init__.py for installation

#### Changed

- New installation. Now you just put your code `Library  WatchUI` and you can work :-)
- Repair some bugs in code (Doesnt delete test img, hard instalation, bad assertion in create area keywords etc.)
- Repair bugs in documentation


### 1.0.5 - 2020-08-22

#### Added

- New keywords rotate image

### 1.0.0 - 2020-05-04

#### Added

- standardized RF documentation file generated via libdoc
- added .gitignore file
- added LICENCE file

#### Changed

- unittests moved to new location, separated from WatchUI library file
- unittests .robot file changed to reflect the move
- WatchUI.py docstrings modified to generate documentation via libdoc
- minor refactoring of WatchUI.py to remove redundant variable assignments
- modified unittests github pipeline to reflect unittests move

### 0.17.8 - 2020-04-10

#### Added

- Created new unit test for starting CI
- Added screen in robot framework log if the test is pass
- Created Actions on github.com

#### Changed

- Change in code (more OOP)

### 0.17.2 - 2020-03-25

#### Added

- SSIM (Threshold) and outputs folder can be set in **_ settings _** (Library output_foder= ssim=)
- With settings we must change code, so now you can find class in ours code :-)
- Keyword Create Area has screen_name now
- Every keyword for compare has settings for lowest limit of difference. ssim=

#### Changed

- Changed outputs folder from name by keyword name, just on ../Outputs
- Repair bug in keyword Compare screen get info. Now if you set bad path, give you error
- Change ssim from int to float
- Others change in code

### 0.16.4 - 2020-03-19

#### Changed

- Change keyword `Compare making rescreens` on `Create sreens`
- Change keyword `Compare making are` on `Create area`
- Change name folder in keyword Create screens from `name_screen` on `screen_name`
- Fixed keyword in test.robot
- Some change in code
- Add new creator Radek Bednařík in code, thanks for help :-)
- Fixed bugs in area keywords
- After install with pypi u can using with full apth your watchUI in robot framework

### 0.14.1 - 2020-03-18

#### Added

- Add settings for Compare making rescreens. Now you can set up name for folder and picture.

#### Changed

- Fixed some log to robot
- Fixed readme
- Fixed error in test.robot (Library Watchmen -> Library WatchUI)
- Fixed and change documentations

