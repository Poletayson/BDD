# Created by Дима at 09.04.2019
Feature: Image converter
New Python  Image converter

  Scenario:
    Given I have my Image converter C:/Users/Дима/Desktop/test/1.jpg
    When I have opened image
    Then The result should be jpg

   Scenario:
    Given I have my Image converter C:/Users/Дима/Desktop/test/3.png
    When I have opened image
    Then The result should be png

   Scenario:
    Given I have my Image converter C:/Users/Дима/Desktop/test/2.jpeg
    When I have opened image
    Then The result should be jpeg

