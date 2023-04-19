# Created by lion7 at 4/18/2023
Feature: Test Scenarios for functionality
  # Enter feature description here

  Scenario: Koel | User should be able to create Smart playlist with not existing song in app with one rule
    # Enter steps here
    Given Open Koel Log In Page
    When Input andrewkoss08@gmail.com11 to email field
    And Iput Andriikoss1! to password field
    And Click to LogIn button
    When Move mose to sin "Create new playlist"
    And  Click to menu new smart playlist
    When Enter smart playlist name New_list11
    And Select fist (model) rule "Title"
    And Select second (operator) rule "is"
    And Enter third (value) rule 5
    And Click to Playlist "SAVE" button
    Then Verify playlist New_list11 is created