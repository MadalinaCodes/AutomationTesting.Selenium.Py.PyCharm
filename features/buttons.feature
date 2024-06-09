Feature: Buttons capability

  Background:
    Given buttons: I am a user on buttons page


  @buttons
  Scenario: I use the first button
    When buttons: I double click the first button
    Then buttons: I validate that first message is displayed


  @buttons
  Scenario: I use the second button
    When buttons: I right click the second button
    Then buttons: I validate that second message is displayed


  @buttons
  Scenario: I use the third button
    When buttons: I click on the third button
    Then buttons: I validate that third message is displayed
