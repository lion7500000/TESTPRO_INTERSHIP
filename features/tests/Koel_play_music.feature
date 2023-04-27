# Created by lion7 at 4/25/2023
Feature: Test Scenarios for functionality
  # Enter feature description here

  Scenario: Koel play music
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com11 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    When Click to song "Dark Days"
    And Click to play music btn
    Then Wait the sound bar