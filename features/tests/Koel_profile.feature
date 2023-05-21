# Created by lion7 at 5/20/2023
Feature:  Test Scenarios for functionality
  # Enter feature description here

  Scenario: Koel | Profile | User should be able to change Theme("Violet")
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com11 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    When Click to profile menu
    And User selects the theme "Violet" on Profile
    Then The frame appears

  Scenario: Koel | Profile | User should be able to change Theme("Rocky")
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com11 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    When Click to profile menu
    And User selects the theme "Rocky" on Profile
    Then The frame appears

  Scenario: Koel | Profile | Confirmation window when closing Koel app should appear when the 'Confirm before closing Koel' checkbox is marked
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com11 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    When Click to profile menu
    And User marks checkbox "Confirm before closing Koel"
    And Click to LogOut button

