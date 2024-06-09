Feature: Auto-complete capability

  Background:
    Given home: I am a user on home page
    When home: I click widgets card
    When widgets: I click Auto Complete

#  @auto
#  Scenario: Validate correct URL
#    Then auto-complete: I should land on auto-complete page

  @auto
  Scenario Outline: I validate that the auto complete is working
    When auto-complete: I introduce "<query>"
    Then auto-complete: I validate that proper color is displayed for "<query>"

    Examples:
      | query |
      | Y     |

