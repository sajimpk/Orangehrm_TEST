Feature: Login functionality
  Scenario: Valid user can login successfully
    Given I am on the login page
    When I enter username "Admin" and password "admin123"
    And I click on the login button
    Then I should see the dashboard page
