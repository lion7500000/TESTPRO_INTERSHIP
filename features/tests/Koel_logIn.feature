# Created by lion7 at 4/7/2023
Feature: Test Scenarios for functionality
  # Enter feature description here

  Scenario: Log In to Koel
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com11 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    Then Verify LogOut button present

