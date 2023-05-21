# Created by lion7 at 4/7/2023
Feature: Test Scenarios for functionality
  # Enter feature description here

  Scenario: KOEL | User should be navigated to the Homepage after successful login
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com11 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    Then Verify Home button present

  Scenario: KOEL | User should be able to log in with the updated email
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com11 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    When Click to profile menu
    And Enter email: andrewkoss08@gmail.com22
    And Enter current password:Andriikoss1!
    And Click to save button
    And Click to LogOut button
    Then Waiting for the LogIn button to be active
    When Input andrewkoss08@gmail.com22 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    Then Verify Home button present

  Scenario: KOEL | User should not be able to log in with old email
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com22 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    Then Wait status logIn fail

  Scenario: KOEL | User should be able to login with the updated password
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com22 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    When Click to profile menu
    And Enter email: andrewkoss08@gmail.com22
    And Enter current password:Andriikoss1!
    And Enter new password:Andriikoss11!
    And Click to save button
    And Click to LogOut button
    Then Waiting for the LogIn button to be active
    When Input andrewkoss08@gmail.com22 to email field
    And Iput Andriikoss11! to password field
    And Click to LogIn button
    Then Verify Home button present

  Scenario: KOEL | User should not be able to log in with old password
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com22 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    Then Waiting for the LogIn button to be active
