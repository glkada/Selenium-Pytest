Feature: Registration functionality

  Scenario: Successful registration and login
    Given I open the registration page
    When I register with credentials
    Then I should be able to login successfully from the login page
