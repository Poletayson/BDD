# Created by Дима at 09.04.2019
Feature: Image converter
New Python  Image converter

  Scenario:
    Given I have my Image converter "C:/Users/Дима/Desktop/test/1.jpg"
    When I have opened image
    Then The result should be jpg

    #And I have saved 20 as second operand