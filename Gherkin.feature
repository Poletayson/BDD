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

    Scenario:
    Given I have my Image converter C:/Users/Дима/Desktop/test/ЛР №5.doc
    When I have opened image
    Then The result should be ...

    Scenario:
    Given I have my Image converter C:/Users/Дима/Desktop/test/1.jpg
    When I have opened image
    And I have saved image C:/Users/Дима/Desktop/test/11.jpg
    Then The result should be jpg

    Scenario:
    Given I have my Image converter C:/Users/Дима/Desktop/test/1.jpg
    When I have opened image
    And I have saved image C:/Users/Дима/Desktop/test/11.png
    Then The result should be png

    Scenario:
    Given I have my Image converter C:/Users/Дима/Desktop/test/3.png
    When I have opened image
    And I have saved image C:/Users/Дима/Desktop/test/33.jpeg
    Then The result should be jpeg

    Scenario:
    Given I have my Image converter C:/Users/Дима/Desktop/test/1.jpg
    When I have opened image
    And I have resized image by W
    Then The size should be 1280, 1280

    Scenario:
    Given I have my Image converter C:/Users/Дима/Desktop/test/2.JPEG
    When I have opened image
    And I have resized image by W
    Then The size should be 640, 640

    Scenario:
    Given I have my Image converter C:/Users/Дима/Desktop/test/3.png
    When I have opened image
    And I have resized image by W
    Then The size should be 618, 618

    Scenario:
    Given I have my Image converter C:/Users/Дима/Desktop/test/ЛР №5.doc
    When I have opened image
    And I have resized image by W
    Then The size should be 0, 0