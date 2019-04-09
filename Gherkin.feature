# Created by Дима at 09.04.2019
Feature: Image converter
New Python  Image converter

  Scenario: # Enter scenario name here
    Given I have my Image converter
    When I have opened image "1.jpg"
    Then The result should be "jpg"

    #And I have saved 20 as second operand