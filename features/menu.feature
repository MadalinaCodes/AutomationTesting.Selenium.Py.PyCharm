Feature: Menu capability

  Background:
    Given home: I am a user on home page
    When home: I click bookstore application card

  @menu
  Scenario: I navigate to Buttons page
    When books: I click Elements
    When books: I click Buttons
    Then buttons: I check that the URL is correct

  @menu
  Scenario: I navigate to Web Tables page
    When books: I click Elements
    When books: I click Web Tables
    Then webtables: I check that the URL is correct

  @menu
  Scenario: I navigate to Auto Complete page
    When books: I click Widgets
    When books: I click Auto Complete
    Then auto-complete: I validate the URL

