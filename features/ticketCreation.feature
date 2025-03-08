Feature: Ticket Creation
  As a registered user,
  I want to create a ticket on the platform
  So that I can see my ticket in the list and track my issues.

  Scenario: Successfully create a ticket and verify it appears in the list
    Given I log in to the platform with valid credentials
    When I navigate to the ticket creation tab
    And I enter <title> in the title field and <description> in the description field, then submit the form
    Then I should be able to see a ticket with the title: <title>

        Examples:
      | title         | description                                         |
      | Issue Title 1 | We can try to solve your problems                   |
      | Issue Title 2 | Maybe the problem you think isn't the actual problem|