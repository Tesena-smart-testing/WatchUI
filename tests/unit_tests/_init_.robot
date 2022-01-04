*** Settings ***
Documentation                   Suite description
Library                         Screenshot
Library                         WatchUI
Library                         String
Library                         OperatingSystem


Resource                        settings/resources.robot
Resource                        resources/keywords.robot


#Test Setup                      Suite Setup
#Test Teardown                   Close web-browser

#   robot -d Results tests/tests_v2.robot
#   robot -d Results -i fix tests/tests_v2.robot

#stalo by za to vsude pridat screen name
#neumi porovnat obrazek 2 rozdilnuch formatu, i kdyz jsou stejne
*** Test Cases ***
 Suite Setup
    Remove directory  ${result_files}  recursive=True
    Directory should not exist   ${result_files}

    create directory  ${result_files}
    Directory should exist  ${result_files}

