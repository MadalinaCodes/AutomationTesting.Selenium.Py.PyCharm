#Feature: Auto-complete capability
#
#  Background:
#    Given home: I am a user on home page
#    When home: I click bookstore application card
#    When books: I click Widgets
#    When books: I click Auto Complete
#
#  @auto
#  Scenario: Validate correct URL
#    Then auto-complete: I check that the URL is correct
#
#  @auto
#  Scenario: I validate that the auto complete is working
#    When auto-complete: I introduce "<query>"
#    Then auto-complete: I validate that the "<suggestion>" is displayed
#
#    Examples:
#      |query| suggestion |
#      |W    | White      |
#      |Y    | Yellow     |
#      |P    | Purple     |
#      |V    | Violet     |
#      |I    | Indigo     |
#      |M    | Magenta    |
#      |Gr   | Gray       |
#      |O    | Orange     |
#      |B    | Beige      |
#
##    |query|
##    |W    |
##    |Y    |
##    |P    |
##    |V    |
##    |I    |
##    |M    |
##    |Gr   |
##    |O    |
##    |B    |
#
##  @auto
##  Scenario: I validate that the auto complete is working
##    When auto-complete: I introduce w
##    Then auto-complete: I validate that the color name is displayed