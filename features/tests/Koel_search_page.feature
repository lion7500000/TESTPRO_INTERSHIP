# Created by lion7 at 4/17/2023
Feature: Test Scenarios for functionality
  # Enter feature description here

  Scenario: Koel search song
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com11 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    When Input serch text Ketsa in search fild
    Then Verify search text Ketsa is present

  Scenario: Koel | User should be able to find artists using search field with existing artists
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com11 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    When Input serch text Dan Brasco in search fild
    Then Verify search Artist Dan Brasco is present

  Scenario: Koel | User should be able to find artists using search field with not existing artists
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com11 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    When Input serch text Dina in search fild
    Then Verify search Artist None found.