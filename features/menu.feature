Feature: Menu capability

  Background:
    Given home: I am a user on home page
    When home: I click bookstore application card

  @menu
  Scenario: I navigate to Buttons page
    When books: I click Elements
    When books: I click Buttons
    Then buttons: I check that the URL is correct
